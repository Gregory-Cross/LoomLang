"""Build and run the OCaml bootstrap using only the installed private toolchain.

Run with Python -B. See README.md for the exact commands and scope.
No download, installation or persistent environment change is performed.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import threading
import time
import uuid

PROJECT = Path(__file__).resolve().parent
TOOLCHAIN = Path(r"C:\LoomBuild\toolchains\ocaml-check-20261117-1500")
BUILD_ROOT = Path(r"C:\LoomBuild\codex\loom-compiler")
OCAMLOPT = TOOLCHAIN / "ocaml/bin/ocamlopt.exe"
SLOT = Path(r"C:\Users\grego\mods\loom-build-slot\slot.py")
MODULES = ("bootstrap.mli", "bootstrap.ml", "test_runner.ml")
HOLDER = "codex-y-compiler-" + str(os.getpid()) + "-" + uuid.uuid4().hex[:8]


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def inputs():
    paths = [PROJECT / "build.py", *(PROJECT / "src" / n for n in MODULES)]
    paths += sorted((PROJECT / "fixtures").iterdir())
    return {p.relative_to(PROJECT).as_posix(): sha(p) for p in paths if p.is_file()}


def private_environment(directory):
    # Same process-only environment as Bind's successful check. Relocate every
    # writable home/cache/temp directory into this build, keeping H read-only.
    private = directory / "private"
    values = {
        "HOME": private / "home", "APPDATA": private / "appdata",
        "LOCALAPPDATA": private / "localappdata", "TEMP": private / "tmp",
        "TMP": private / "tmp", "XDG_CONFIG_HOME": private / "home/.config",
        "XDG_CACHE_HOME": private / "home/.cache",
        "XDG_DATA_HOME": private / "home/.local/share",
    }
    for path in values.values():
        path.mkdir(parents=True, exist_ok=True)
    keep = ("SystemRoot", "windir", "SystemDrive", "COMSPEC", "PATHEXT",
            "NUMBER_OF_PROCESSORS", "PROCESSOR_ARCHITECTURE", "OS", "USERNAME")
    env = {key: os.environ[key] for key in keep if key in os.environ}
    env.update({key: str(value) for key, value in values.items()})
    tmp = values["TMP"].as_posix()
    env["TMPDIR"] = "/" + tmp[0].lower() + tmp[2:]
    env.update({"MSYSTEM": "MINGW64", "MSYS2_PATH_TYPE": "strict",
                "CHERE_INVOKING": "1"})
    # This is exactly the successful check's private PATH, not an addition to
    # the user's or the calling process's PATH. No new search folder is needed.
    env["PATH"] = ";".join(str(TOOLCHAIN / p) for p in
                           ("ocaml/bin", "msys64/mingw64/bin", "msys64/usr/bin"))
    env["PATH"] += r";C:\Windows\System32;C:\Windows"
    return env


class MemoryStatus(ctypes.Structure):
    _fields_ = [("length", wintypes.DWORD), ("load", wintypes.DWORD)] + [
        (name, ctypes.c_ulonglong) for name in
        ("total_physical", "available_physical", "total_pagefile",
         "available_pagefile", "total_virtual", "available_virtual", "extended")]


def memory():
    value = MemoryStatus()
    value.length = ctypes.sizeof(value)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(value)):
        raise ctypes.WinError()
    return {"physical_available_bytes": value.available_physical,
            "commit_headroom_bytes": value.available_pagefile}


@contextmanager
def defer_interrupts(pending):
    # A cancellation is delivered after custody/cleanup, never discarded.
    main_thread = threading.current_thread() is threading.main_thread()
    previous = signal.getsignal(signal.SIGINT) if main_thread else None
    if main_thread:
        signal.signal(signal.SIGINT, lambda _signum, _frame: pending.append(KeyboardInterrupt()))
    try:
        yield
    finally:
        if main_thread:
            signal.signal(signal.SIGINT, previous)


def drain_process(proc, pending, timeout=None):
    deadline = None if timeout is None else time.monotonic() + timeout
    while True:
        try:
            remaining = None if deadline is None else max(0, deadline - time.monotonic())
            return proc.communicate(timeout=remaining)
        except (KeyboardInterrupt, SystemExit) as error:
            pending.append(error)


def slot_result(args, pending):
    # Await an interrupted helper before any later cleanup can touch its slot.
    # Tokens are passed only to slot.py and kept in memory, never in this log.
    with defer_interrupts(pending):
        proc = subprocess.Popen([sys.executable, "-B", str(SLOT), *args],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            out, err = drain_process(proc, pending)
        except BaseException:
            while True:
                try:
                    proc.wait()
                    break
                except (KeyboardInterrupt, SystemExit) as error:
                    pending.append(error)
            raise
    return proc.returncode, out, err


def slot_call(args, *, deferred=None):
    pending = [] if deferred is None else deferred
    code, out, err = slot_result(args, pending)
    if code:
        raise RuntimeError("slot.py refused: " + out.strip() + err.strip())
    if deferred is None and pending:
        raise pending[0]
    return out


def cleanup_acquisition(kind, journal):
    # The helper may have acquired before its response was lost or malformed.
    # Its name-only release checks our unique holder name before changing a
    # lock. A refusal for another holder confirms that we do not own that lock.
    pending = []
    code, out, _err = slot_result(["release", HOLDER, "--slot", kind], pending)
    message = out.strip()
    confirmed = (code == 0 and message in ("released", "already free"))
    other_holder = code == 4 and message.startswith("refused: held by ")
    journal.append({"event": "acquire-cleanup", "slot": kind, "utc": utc(),
                    "exit_code": code, "result": message,
                    "owned_hold_absent": confirmed or other_holder})
    if not (confirmed or other_holder):
        raise RuntimeError("slot acquisition cleanup unconfirmed: " + kind)
    if pending:
        raise pending[0]


@contextmanager
def slots(kinds, journal):
    owned = []
    try:
        for kind in kinds:
            try:
                raw = slot_call(["try", HOLDER, "OCaml compiler bootstrap", "--slot", kind, "--json"])
                record = json.loads(raw)
                token = record.pop("token")
                if (record.get("slot") != kind or record.get("holder") != HOLDER
                        or not isinstance(token, str) or len(token) != 64
                        or any(c not in "0123456789abcdef" for c in token)):
                    raise RuntimeError("invalid slot acquisition response")
            except BaseException:
                cleanup_acquisition(kind, journal)
                raise
            owned.append((kind, token))
            journal.append({"event": "acquire", **record,
                            "token_sha256": hashlib.sha256(token.encode()).hexdigest()})
            adoption = slot_call(["adopt", "--slot", kind, "--token", token, "--by", HOLDER])
            journal.append({"event": "adopt", "slot": kind, "record": json.loads(adoption)})
        yield
    finally:
        if any(event.get("event") == "native-cleanup-unconfirmed" for event in journal):
            journal.append({"event": "slots-retained", "utc": utc(), "holder": HOLDER,
                            "slots": [kind for kind, _token in owned],
                            "reason": "native termination unconfirmed; coordinator recovery required"})
        else:
            errors, pending = [], []
            with defer_interrupts(pending):
                for kind, token in reversed(owned):
                    try:
                        result = slot_call(["release", HOLDER, "--slot", kind, "--token", token],
                                           deferred=pending)
                        if result.strip() != "released":
                            raise RuntimeError("token release unconfirmed: " + kind)
                        journal.append({"event": "release", "slot": kind,
                                        "utc": utc(), "result": result.strip()})
                    except BaseException as error:
                        if isinstance(error, (KeyboardInterrupt, SystemExit)):
                            pending.append(error)
                        else:
                            errors.append(kind + ": " + type(error).__name__ + ": " + str(error))
            if errors or pending:
                journal.append({"event": "release-outcome", "utc": utc(), "errors": errors,
                                "deferred": [type(error).__name__ for error in pending]})
            if errors:
                failure = RuntimeError("slot release unconfirmed: " + "; ".join(errors))
                if pending:
                    raise pending[0] from failure
                raise failure
            if pending:
                raise pending[0]


class NativeJob:
    """Own a Windows process tree from its suspended first instruction."""
    class Limits(ctypes.Structure):
        _fields_ = [("process_time", ctypes.c_longlong), ("job_time", ctypes.c_longlong),
                    ("flags", wintypes.DWORD), ("minimum_ws", ctypes.c_size_t),
                    ("maximum_ws", ctypes.c_size_t), ("active_limit", wintypes.DWORD),
                    ("affinity", ctypes.c_size_t), ("priority", wintypes.DWORD),
                    ("scheduling", wintypes.DWORD)]

    class Accounting(ctypes.Structure):
        _fields_ = [(name, ctypes.c_longlong) for name in
                    ("user", "kernel", "period_user", "period_kernel")] + [
                    (name, wintypes.DWORD) for name in
                    ("page_faults", "total_processes", "active_processes", "terminated")]

    class ThreadEntry(ctypes.Structure):
        _fields_ = [(name, wintypes.DWORD) for name in ("size", "usage", "tid", "pid")] + [
                    ("base_priority", wintypes.LONG), ("delta_priority", wintypes.LONG),
                    ("flags", wintypes.DWORD)]

    def __init__(self):
        self.api = ctypes.WinDLL("kernel32", use_last_error=True)
        declarations = {
            "CreateJobObjectW": ([ctypes.c_void_p, wintypes.LPCWSTR], wintypes.HANDLE),
            "SetInformationJobObject": ([wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD], wintypes.BOOL),
            "QueryInformationJobObject": ([wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.c_void_p], wintypes.BOOL),
            "AssignProcessToJobObject": ([wintypes.HANDLE, wintypes.HANDLE], wintypes.BOOL),
            "TerminateJobObject": ([wintypes.HANDLE, wintypes.UINT], wintypes.BOOL),
            "CloseHandle": ([wintypes.HANDLE], wintypes.BOOL),
            "CreateToolhelp32Snapshot": ([wintypes.DWORD, wintypes.DWORD], wintypes.HANDLE),
            "Thread32First": ([wintypes.HANDLE, ctypes.POINTER(self.ThreadEntry)], wintypes.BOOL),
            "Thread32Next": ([wintypes.HANDLE, ctypes.POINTER(self.ThreadEntry)], wintypes.BOOL),
            "OpenThread": ([wintypes.DWORD, wintypes.BOOL, wintypes.DWORD], wintypes.HANDLE),
            "ResumeThread": ([wintypes.HANDLE], wintypes.DWORD),
        }
        for name, (arguments, result) in declarations.items():
            function = getattr(self.api, name)
            function.argtypes, function.restype = arguments, result
        self.handle = self.api.CreateJobObjectW(None, None)
        if not self.handle:
            raise ctypes.WinError(ctypes.get_last_error())
        class ExtendedLimits(ctypes.Structure):
            _fields_ = [("basic", NativeJob.Limits), ("io_counters", ctypes.c_ulonglong * 6),
                        ("process_memory", ctypes.c_size_t), ("job_memory", ctypes.c_size_t),
                        ("peak_process_memory", ctypes.c_size_t), ("peak_job_memory", ctypes.c_size_t)]
        limit = ExtendedLimits()
        limit.basic.flags = 0x2000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        if not self.api.SetInformationJobObject(self.handle, 9, ctypes.byref(limit), ctypes.sizeof(limit)):
            error = ctypes.WinError(ctypes.get_last_error())
            self.close()
            raise error

    def assign(self, proc):
        if not self.api.AssignProcessToJobObject(self.handle, wintypes.HANDLE(int(proc._handle))):
            raise ctypes.WinError(ctypes.get_last_error())

    def resume(self, pid):
        # Popen closes the primary-thread handle. Find only our still-suspended
        # child's primary thread; no thread of another process is opened.
        snapshot = self.api.CreateToolhelp32Snapshot(0x4, 0)  # TH32CS_SNAPTHREAD
        if snapshot == ctypes.c_void_p(-1).value:
            raise ctypes.WinError(ctypes.get_last_error())
        entry = self.ThreadEntry()
        entry.size = ctypes.sizeof(entry)
        try:
            present = self.api.Thread32First(snapshot, ctypes.byref(entry))
            while present:
                if entry.pid == pid:
                    thread = self.api.OpenThread(0x2, False, entry.tid)  # THREAD_SUSPEND_RESUME
                    if not thread:
                        raise ctypes.WinError(ctypes.get_last_error())
                    try:
                        if self.api.ResumeThread(thread) == 0xFFFFFFFF:
                            raise ctypes.WinError(ctypes.get_last_error())
                    finally:
                        self.api.CloseHandle(thread)
                    return
                present = self.api.Thread32Next(snapshot, ctypes.byref(entry))
            raise RuntimeError("owned suspended thread not found")
        finally:
            self.api.CloseHandle(snapshot)

    def terminate(self):
        if not self.api.TerminateJobObject(self.handle, 1):
            raise ctypes.WinError(ctypes.get_last_error())

    def wait_empty(self, timeout=10):
        deadline = time.monotonic() + timeout
        while True:
            accounting = self.Accounting()
            if not self.api.QueryInformationJobObject(self.handle, 1, ctypes.byref(accounting),
                                                     ctypes.sizeof(accounting), None):
                raise ctypes.WinError(ctypes.get_last_error())
            if accounting.active_processes == 0:
                return
            if time.monotonic() >= deadline:
                raise TimeoutError("owned process tree did not terminate")
            time.sleep(0.01)

    def close(self):
        if self.handle:
            handle, self.handle = self.handle, None
            if not self.api.CloseHandle(handle):
                raise ctypes.WinError(ctypes.get_last_error())


def launch(argv, directory, env, journal):
    start = time.perf_counter()
    record = {"argv": [str(a) for a in argv], "cwd": str(directory), "start_utc": utc()}
    samples = [memory()]
    done = threading.Event()
    sample_errors = []

    def sample():
        while not done.wait(0.01):
            try:
                samples.append(memory())
            except Exception as error:
                sample_errors.append(str(error))
                return

    sampler = threading.Thread(target=sample, daemon=True)
    sampler.start()
    proc, job, assigned = None, None, False
    pending, primary, cleanup_error = [], None, None
    stdout, stderr = b"", b""
    try:
        # Deferral covers the hand-off from Popen to job assignment. A child
        # cannot run or create descendants before it belongs to the owned job.
        with defer_interrupts(pending):
            job = NativeJob()
            proc = subprocess.Popen(record["argv"], cwd=directory, env=env,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    creationflags=subprocess.CREATE_NO_WINDOW | 0x4)  # CREATE_SUSPENDED
            record["pid"] = proc.pid
            job.assign(proc)
            assigned = True
            job.resume(proc.pid)
        if pending:
            raise pending.pop(0)
        try:
            stdout, stderr = proc.communicate(timeout=60)
        except subprocess.TimeoutExpired:
            record["timed_out"] = True
            raise TimeoutError("native command timed out: " + str(argv[0]))
    except BaseException as error:
        primary = error
    finally:
        with defer_interrupts(pending):
            try:
                if proc is not None:
                    if assigned:
                        job.terminate()
                    else:
                        # It never left CREATE_SUSPENDED, so it has no children.
                        proc.kill()
                    stdout, stderr = drain_process(proc, pending, timeout=10)
                    if job is not None:
                        job.wait_empty()
                    if proc.poll() is None:
                        raise RuntimeError("native root exit unconfirmed")
                    record["tree_termination_confirmed"] = True
                    record["tree_drained_utc"] = utc()
            except BaseException as error:
                cleanup_error = error
                journal.append({"event": "native-cleanup-unconfirmed", "utc": utc(),
                                "pid": None if proc is None else proc.pid,
                                "error": type(error).__name__ + ": " + str(error)})
            finally:
                if job is not None:
                    try:
                        job.close()
                    except BaseException as error:
                        if cleanup_error is None:
                            cleanup_error = error
                        journal.append({"event": "native-cleanup-unconfirmed", "utc": utc(),
                                        "pid": None if proc is None else proc.pid,
                                        "error": "job close: " + type(error).__name__})
                done.set()
                sampler.join()
                try:
                    samples.append(memory())
                except Exception as error:
                    sample_errors.append(str(error))
                record.update(exit_code=None if proc is None else proc.returncode,
                              stdout=stdout.decode("utf-8", "replace"), stderr=stderr.decode("utf-8", "replace"),
                              stdout_sha256=hashlib.sha256(stdout).hexdigest(),
                              stderr_sha256=hashlib.sha256(stderr).hexdigest(),
                              exception=None if primary is None else type(primary).__name__,
                              deferred_interruptions=[type(error).__name__ for error in pending],
                              end_utc=utc(), wall_seconds=time.perf_counter() - start,
                              memory_samples=len(samples), memory_sample_errors=sample_errors,
                              physical_available_min=min(s["physical_available_bytes"] for s in samples),
                              commit_headroom_min=min(s["commit_headroom_bytes"] for s in samples))
                journal.append({"event": "process", **record})
    if cleanup_error is not None:
        raise RuntimeError("native cleanup unconfirmed; slots retained for coordinator recovery") from cleanup_error
    if primary is not None:
        raise primary
    if pending:
        raise pending[0]
    return record


def checked_directory(raw):
    directory = Path(raw).resolve()
    if directory.parent != BUILD_ROOT.resolve():
        raise ValueError("build directory must be an immediate child of " + str(BUILD_ROOT))
    return directory


def execute(args, directory, journal):
    if args.action == "build":
        if args.kind == "clean":
            directory.mkdir(parents=True, exist_ok=False)
        elif not (directory / "BUILD-BINDINGS.json").is_file():
            raise ValueError("rebuild requires a successful prior build")
    elif not (directory / "BUILD-BINDINGS.json").is_file():
        raise ValueError("test requires a successful build")
    env = private_environment(directory)
    before = inputs()
    result = {"action": args.action, "directory": str(directory),
              "source_bindings": before, "environment": env,
              "jobs": 1, "jobs_reason": "explicit ordered modules; no parallel compiler driver",
              "toolchain": str(TOOLCHAIN), "ocamlopt_sha256": sha(OCAMLOPT)}
    if args.action == "build":
        result["kind"] = args.kind
        # Test code generation holds build, then run, as slot.py requires.
        with slots(("build", "run"), journal):
            version = launch([OCAMLOPT, "-version"], directory, env, journal)
            if version["exit_code"]:
                return version["exit_code"], result
            result["ocaml_version"] = version["stdout"].strip()
            for name in MODULES:
                (directory / name).write_bytes((PROJECT / "src" / name).read_bytes())
                compiled = launch([OCAMLOPT, "-w", "+a-70", "-warn-error", "+a-70",
                                   "-c", name], directory, env, journal)
                if compiled["exit_code"]:
                    return compiled["exit_code"], result
            linked = launch([OCAMLOPT, "bootstrap.cmx", "test_runner.cmx", "-o", "test_runner.exe"],
                            directory, env, journal)
            if linked["exit_code"]:
                return linked["exit_code"], result
            if inputs() != before:
                raise RuntimeError("source changed during build")
            save(directory / "BUILD-BINDINGS.json",
                 {"inputs": before, "executable_sha256": sha(directory / "test_runner.exe")})
        return 0, result
    if Path(args.suite).name != args.suite or args.suite in (".", ".."):
        raise ValueError("suite must be a fixture file name")
    with slots(("run",), journal):
        # A writer can finish between our initial checks and this acquisition.
        # Validate the current artifact only while its replacement is excluded.
        bindings = json.loads((directory / "BUILD-BINDINGS.json").read_bytes())
        executable_sha256 = sha(directory / "test_runner.exe")
        if bindings["inputs"] != before or bindings["executable_sha256"] != executable_sha256:
            raise RuntimeError("build is stale or executable bytes changed")
        result["executable_sha256"] = executable_sha256
        tested = launch([directory / "test_runner.exe", "--fixtures", PROJECT / "fixtures",
                         "--suite", PROJECT / "fixtures" / args.suite], directory, env, journal)
    if inputs() != before:
        raise RuntimeError("source changed during test")
    result.update(suite=args.suite, test_stdout=tested["stdout"], test_stderr=tested["stderr"])
    return tested["exit_code"], result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    build = commands.add_parser("build")
    build.add_argument("--kind", choices=("clean", "rebuild"), required=True)
    build.add_argument("--directory", required=True)
    test = commands.add_parser("test")
    test.add_argument("--directory", required=True)
    test.add_argument("--suite", required=True)
    args = parser.parse_args()
    directory = checked_directory(args.directory)
    journal = []
    start = time.perf_counter()
    result = {"action": args.action, "start_utc": utc()}
    code = 2
    try:
        code, details = execute(args, directory, journal)
        result.update(details)
    except Exception as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    finally:
        result.update(exit_code=code, end_utc=utc(), wall_seconds=time.perf_counter() - start,
                      journal=journal, python_version=sys.version)
        if directory.is_dir():
            logs = directory / "logs"
            logs.mkdir(exist_ok=True)
            log = logs / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%f") + ".json")
            save(log, result)
            result["log"] = str(log)
        print(json.dumps(result, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
