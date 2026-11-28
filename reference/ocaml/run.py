"""Build and run the Windows x64 OCaml increment 1 reference evaluator."""

import argparse
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from threading import Lock
import time


HERE = Path(__file__).resolve().parent
MODULES = ("nat", "json", "probe_switch", "core", "resolved_graph", "arithmetic", "driver")
INTERFACES = ("nat", "json", "core", "resolved_graph", "arithmetic")
OBSERVERS = ("ordinary", "trial-exact")
MINGW = Path("msys64/mingw64")
OCAML_BIN = Path("ocaml/bin")
STDLIB = Path("ocaml/lib/ocaml")
OPT = OCAML_BIN / "ocamlopt.opt.exe"
DEP = OCAML_BIN / "ocamldep.opt.exe"
GCC = MINGW / "bin/x86_64-w64-mingw32-gcc.exe"
COMPILE_FLAGS = ("-verbose", "-c")
LINK_FLAGS = ("-verbose", "-ccopt", "-v", "-ccopt", "-link", "-ccopt", "-v",
              "-ccopt", "-link", "-ccopt", "-Wl,--no-insert-timestamp,-t")
LOG_LIMIT = 8 << 20
STREAM_LIMIT = 8_000_000

# Each lock row gives SHA-256, byte count and a distribution-relative path.
TOOLCHAIN_LOCK = """\
be9b3cba24ef373e836e8cffad5fdfa763e199b322f4657ca37d3c3bdcead431 1971059 msys64/mingw64/bin/as.exe
28af7c96b3de562d11910b6b19398d454664ad6e5279442c65248ac03f0031f2 3301173 msys64/mingw64/bin/gcc.exe
e5f877e604846435aedd5b1dedf9b62fbde7cfe24b65625a3d6f0d8f76ff5f80 1932716 msys64/mingw64/bin/ld.exe
317a714680dd0706c4f56c06fe23a6a9af2a7703120066845c7fd4a4e8841a5d 141183 msys64/mingw64/bin/libasprintf-0.dll
d057f3ef0932f937093bcde39e478dce31f308406f999fa963c3614ed89d9498 42734 msys64/mingw64/bin/libcharset-1.dll
661f70dc19fde8c25bb56387b807b7a9ab7e532cf58fa8aeee078256c19d8980 149364 msys64/mingw64/bin/libgcc_s_seh-1.dll
37248cda33845e7c5c35a574e57da762dd0a8268f0270d179f30a33746809681 679747 msys64/mingw64/bin/libgmp-10.dll
9a667d5dc4ca5a49d1d5fdbfa83866e0e04fbab1c304b49b67951498159a8246 30824 msys64/mingw64/bin/libgmpxx-4.dll
587bd8c780e89f5d834c251accc6053f479713184c433e0f1bab898ee0aa3751 1141004 msys64/mingw64/bin/libiconv-2.dll
0537c3dd2378218508ebe3cc416d72a99ee2d24ae1c5525e23458f32544ef861 298731 msys64/mingw64/bin/libintl-8.dll
c00727a1d632a2c67fa90a06665c1759d73eb2d5137831986cafc014cbe2fa70 2331962 msys64/mingw64/bin/libisl-23.dll
3a1d4c692c7a2af929ae043a2c88903304b84917bd84ca46bf75bb5389b11be8 162742 msys64/mingw64/bin/libmpc-3.dll
ed5f7bdf777f0f6af00ba193ce4b04e12efa787245a946a631db736e49c0bb1a 715191 msys64/mingw64/bin/libmpfr-6.dll
b720a96289bcd6d9ec6f5f1f5612f1b1a523ce15d3ada20fe119791274cb512f 2659216 msys64/mingw64/bin/libstdc++-6.dll
98a4fea591385952cad1c532f4a92606358630976e9ede5fcf115ab945305a09 73020 msys64/mingw64/bin/libwinpthread-1.dll
b82cab3e02b60e664c19eb3459f6e6ca7f6165a727bbb18f48dee0474b42a920 148872 msys64/mingw64/bin/libz-1.dll
c574abadf7e95bd16ee4e96a3fb9dccb6106b65a958fae0e592a9c69895fe6d5 191257 msys64/mingw64/bin/libzlibwapi.dll
b95c223a9548a9ecf51377c962e0bc8f0c51eb0c6f67a296dbc885996f0dd40d 1218273 msys64/mingw64/bin/libzstd.dll
28af7c96b3de562d11910b6b19398d454664ad6e5279442c65248ac03f0031f2 3301173 msys64/mingw64/bin/x86_64-w64-mingw32-gcc.exe
72df18f3a7c8e9341c776a5a23c2dfb2524dbbf1f343c3012cb1178436535a29 191257 msys64/mingw64/bin/zlib1.dll
26491145fcd72c0be6d12f647ceffc59e04d7d6e1ad40f68888b5097c1fdea36 39374994 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/cc1.exe
5cde40b65e64cd6e3a0f2aa8a0d90860be6aa538f0b8f76db783b6bb79197daa 2350340 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/collect2.exe
3e9a96dab213b41c8f5993146d11d709d0d3ea0b4758746b588582cec3c6a35f 152088 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/liblto_plugin.dll
be9b3cba24ef373e836e8cffad5fdfa763e199b322f4657ca37d3c3bdcead431 1971059 msys64/mingw64/x86_64-w64-mingw32/bin/as.exe
e5f877e604846435aedd5b1dedf9b62fbde7cfe24b65625a3d6f0d8f76ff5f80 1932716 msys64/mingw64/x86_64-w64-mingw32/bin/ld.exe
d771998e92f643e3e2d4f57e48c38719c93ade8b722867b2720386e3400ad930 4504471 ocaml/bin/flexlink.exe
d771998e92f643e3e2d4f57e48c38719c93ade8b722867b2720386e3400ad930 4504471 ocaml/bin/flexlink.opt.exe
d29a92ee17c48d8c7fcf79f260038b6cbebf0d459a0a67582e359bf2decbe266 14238099 ocaml/bin/ocamldep.opt.exe
48887da046219b2aae67120da66f014b5f9c0eebd981fee50229ae3e5a6a06ae 17682795 ocaml/bin/ocamlopt.opt.exe
d4724be481f46ea7a7ea1b178ae694b8cb01ac84bd9f9ca5e22c570130aa7257 3659 ocaml/lib/ocaml/camlinternalFormat.cmi
413c53a69affcd2c55bd9033560651bc0856cd441abe53012a2dee068df53916 8870 ocaml/lib/ocaml/camlinternalFormat.cmx
01f6a0435e7d097f6c9d69382f6da36c5ac16e1157576cb6e111f5aa275da70b 8507 ocaml/lib/ocaml/camlinternalFormatBasics.cmi
3fed3f000d04525b7bc7c149da38dedd22384fa0485d2cb8242299a0e887e39f 341 ocaml/lib/ocaml/camlinternalFormatBasics.cmx
148813627c5f503ea611260b76f70012c5a4360eb15585c7f9aea2099116a590 552 ocaml/lib/ocaml/camlinternalLazy.cmi
dcc00cc92fa9d8e4a13584b123eb7fc2902aa26f5b42e6a6b448a728f8759d69 834 ocaml/lib/ocaml/camlinternalLazy.cmx
bcc99c8be737bb91a5224639e247b20a1d81cf144453c0fa83155e87b83d93d4 713 ocaml/lib/ocaml/camlinternalMod.cmi
83780ca58350800dbd653b1e2b2701147d064a6b39c394825839555cec933d63 861 ocaml/lib/ocaml/camlinternalMod.cmx
4fd04c19d35cf508277da74a2267651853904a4b51d5b143ce04b3b1be98c84f 3374 ocaml/lib/ocaml/camlinternalOO.cmi
171358c60c78dc54e6d79fadf041003dafb5b13d327897b9f89bdb83111230ab 7439 ocaml/lib/ocaml/camlinternalOO.cmx
3d4c91fdc81cd6f887f3f102a265ad29e08f72c947eac27e16b1d5610b45ab5f 1611 ocaml/lib/ocaml/flexdll/flexdll_initer_mingw64.o
f09fb5f2479d7e3b5b2bde6fb56fffea1cd395b4428808c71e0be553d7079dfa 13066 ocaml/lib/ocaml/flexdll/flexdll_mingw64.o
ab3b764192045a6fc47a515075706a72a8a8f6104c684c0ff6f4e71a2a0a08d2 2617716 ocaml/lib/ocaml/libasmrun.a
65683996a0f4b1e510f16e3a7bad151322dc77e8889982e0cb842829de1f5d25 2893334 ocaml/lib/ocaml/libasmrund.a
d5a08ba515e99e6a3b160abc959247c65817efa3cf9f11d6cd8ef6dc5f947aee 2734752 ocaml/lib/ocaml/libcamlrun.a
a5de6987105d91ac6eedf2ec3f3711fd0c6ef6139c49e326fabdedf464c2a33f 3061632 ocaml/lib/ocaml/libcamlrund.a
7e239723c279cbb030a7c694f936b5df2da829b6f3a73c229d6b5f3803b5b3e1 79888 ocaml/lib/ocaml/libcamlruntime_eventsbyt.a
71520e7f0f4f551b90438bec2140ba599d1c9c8fb36d7564933aa204448d9cce 79924 ocaml/lib/ocaml/libcamlruntime_eventsnat.a
dbf8c910d22ac007c8492771bd8f9e3e2a9f66bdad24fd7c9d63f64d86be3b14 28660 ocaml/lib/ocaml/libcamlstrbyt.a
7c9a909dfc2c7f8a1664f9fbb74ae3e1ae98f397d475b4052bdb6b1908730288 28692 ocaml/lib/ocaml/libcamlstrnat.a
ba399b7b8ad90bc5a8b2429a084e49cc3a08a14599c2ee5d709d9a7a1b6d6dc4 8852 ocaml/lib/ocaml/libcomprmarsh.a
c673ce4e50f145f247667495e9972c16ed674c87f94426d277166439f403912e 69128 ocaml/lib/ocaml/libthreads.a
e51fa40257767518318d77c1219c986f483abdde92637f1e1558ab1d6142440d 68352 ocaml/lib/ocaml/libthreadsnat.a
a19a9e1ecb3e7bfcf4dc0b6fea18dd8cd67d066de2f25871a4baf5ad5bdc0a57 796476 ocaml/lib/ocaml/libunixbyt.a
1d8013f94e2ee279eb6e4b19866d8c257712c9734a10ab565c1cd9700bff4b72 799096 ocaml/lib/ocaml/libunixnat.a
0d0bcb3cd3fc57a4f80fad7845995fe379b4767bab3c46c314e52b04b08c7414 188 ocaml/lib/ocaml/std_exit.cmi
dd38933802edc7484341bb36eaf943e282e989230e5352942a53206f9b5701bc 200 ocaml/lib/ocaml/std_exit.cmx
e74bf777fef384dcc9a18ac4cb124a48856029d7ae633c25a66e0bfee41db781 1206 ocaml/lib/ocaml/std_exit.o
3c38289120ce777e0d4a4b5c45ac01deb4f6830c8c2cfd75411e1c310660ddb0 2240832 ocaml/lib/ocaml/stdlib.a
2af0c91953b4149fb1c4560c77a1334dfcc9eaa112e9217476c526480b17bdf8 13817 ocaml/lib/ocaml/stdlib.cmi
842fe4e8ceb9e9fd1f658cc65b47d58e856e30a98f064df6f712c0eb68a3a9b9 8026 ocaml/lib/ocaml/stdlib.cmx
08106e9e7e183bfa0fc59ad60532f33e4eda3f1d71e758134b87f4d39066782c 30943 ocaml/lib/ocaml/stdlib.cmxa
77f4303b0ed9ecd0cd9780d3a6f0e08794f1de9da7a73ddf4f07326edec29b63 2181 ocaml/lib/ocaml/stdlib__Arg.cmi
9711e848279f02459d477123694eac8202cacecfdc9fb82340a4b9c389e358f2 3250 ocaml/lib/ocaml/stdlib__Arg.cmx
b37215495a6cf38fe7f1112ef79e1f3303717d0b037c119ea8d033470f3737a2 3867 ocaml/lib/ocaml/stdlib__Array.cmi
cffc89f393a9b9e963427606057761d9c7ba13bf4d1235da991abac6f72a1c72 3277 ocaml/lib/ocaml/stdlib__Array.cmx
3f406b316bccc4852fe0de7f2955d7b5f26dde7a7933596c50f313c75d969714 3959 ocaml/lib/ocaml/stdlib__ArrayLabels.cmi
4e64ff46bfa7e0c5c1dda329fde1eb56019ebd8fcfaf3dbd3d20fae10b716e04 2667 ocaml/lib/ocaml/stdlib__ArrayLabels.cmx
1483d89fc1e03a39a919f1e7062e09e849493ba98b14989e1326a6a5879b3edb 1153 ocaml/lib/ocaml/stdlib__Atomic.cmi
a9336e76973049ef9cfa3c16e6d96a9e0f7ab1b7abc7a404e6b34dd914abfbc0 2026 ocaml/lib/ocaml/stdlib__Atomic.cmx
e6b0f2e654fe593c7ba3515972b12ccf013fe713d35f95ff3cf05ebfee49cdc4 8792 ocaml/lib/ocaml/stdlib__Bigarray.cmi
f98da1c44bc336a625bad7787a1b8604564d77b35372ab02dfce2dd5ace3922f 4062 ocaml/lib/ocaml/stdlib__Bigarray.cmx
bd9edfc454df1936888b1533611eb6f077da8d5bc766eea2a6532602a3b094bf 900 ocaml/lib/ocaml/stdlib__Bool.cmi
6278bf875d6062e6873dcf79f768184e2cb61ff23b07ff98f3fffbd488db1961 1286 ocaml/lib/ocaml/stdlib__Bool.cmx
ee3e9e6fff3e2db0bc0401c22db0a7d2be223a72ac29875a35465ff9d50d2211 2193 ocaml/lib/ocaml/stdlib__Buffer.cmi
eefac67180d9b687bc62798bf25e848f4ed990711adebafeacd8e771687f0ee7 10332 ocaml/lib/ocaml/stdlib__Buffer.cmx
69078cfeef1581d1038ae62951b59ef14484c0debf11875302833d56594eb5b2 4894 ocaml/lib/ocaml/stdlib__Bytes.cmi
94f3fffec5e60877b625e7ead7f324ef8cbddfa6894f4261f78f08adeef5ad31 13953 ocaml/lib/ocaml/stdlib__Bytes.cmx
b4132cc2bb88e2b34270cfe288e59d5fe31777f90ea3fded492d6d29d004fa88 4990 ocaml/lib/ocaml/stdlib__BytesLabels.cmi
cf607d3acf6312b34084124ebabebcab1f5a0c13f69b60cc7abdbc618068e1cd 9725 ocaml/lib/ocaml/stdlib__BytesLabels.cmx
742a1156a0d816cee2409ea1b9fa663fe9062e51a9379de18fe6c21760b2b03d 408 ocaml/lib/ocaml/stdlib__Callback.cmi
1e009dbf41230b6f106c14a3c3030c00ef64fa6cf2f7e409b89d3813caec77f7 561 ocaml/lib/ocaml/stdlib__Callback.cmx
8276f07371201828f9e7738a91ee0a7ff74d1bd92a7fca09f79944ac001f8203 1436 ocaml/lib/ocaml/stdlib__Char.cmi
58e0db04f5723af36e2dedff92b81827672eb3018d0b975bfbf147081dec993f 2249 ocaml/lib/ocaml/stdlib__Char.cmx
418d2b1c39d8f283b38bcb19f3fa417923c549b49057166f5d79727638913219 941 ocaml/lib/ocaml/stdlib__Complex.cmi
e467882b274b1d02feb826b7cc01c9d85d1370899ebee43a7b18e86a3136e816 2055 ocaml/lib/ocaml/stdlib__Complex.cmx
41faf95ead52f7e53ba394ceda7e71a09f4ce77f40e7481719e140b6046019cb 542 ocaml/lib/ocaml/stdlib__Condition.cmi
b4e8504b597823ecfeb6b09067bd86c7ee14f0a553a877f797c8057e476f17dc 592 ocaml/lib/ocaml/stdlib__Condition.cmx
7a5c866dedadff815c4f00782b0ef6d19faac90b5d010855f2d594ad15857435 1526 ocaml/lib/ocaml/stdlib__Digest.cmi
445cf62fe7709e8f8f3c0c5a8f3d80ed8f54e6dbb2da13554ea5efcfc4e3a67c 2713 ocaml/lib/ocaml/stdlib__Digest.cmx
6267151d6d30262d3d399fd9713cb7927bc8be57b950028de90f3e4de1dbbf8b 1194 ocaml/lib/ocaml/stdlib__Domain.cmi
267f808fb9b0188699c82a88e23da9acde78697e8111611732d25abbe75311e3 2800 ocaml/lib/ocaml/stdlib__Domain.cmx
5692bfc3ba980ad33ff983228b35bd85f67c0db5db621d99cd3b7aefb220f429 3483 ocaml/lib/ocaml/stdlib__Dynarray.cmi
e4d9bc9f590b4e492d1d754567a70256375842066f536bbb7bef5311c2904307 8301 ocaml/lib/ocaml/stdlib__Dynarray.cmx
b3ab2dd600fecc57016ce4b21fc37e30318f89d90f3129b46acc4c11780ec87e 2091 ocaml/lib/ocaml/stdlib__Effect.cmi
da69dec0250be4e50146dba4f9067d7aa7926c2b72ff18d471f7188df2027c1d 1309 ocaml/lib/ocaml/stdlib__Effect.cmx
e81ae7ce18c91801f7316524ef558d4a654b9c9dacc426d0e3cbec596ae8104c 1438 ocaml/lib/ocaml/stdlib__Either.cmi
079209e27638ec83a4ade74d99b5a408b75091e18fbbcbb84b3690b949a80aed 1723 ocaml/lib/ocaml/stdlib__Either.cmx
81c48446ff8feccf380b11a8da9eee236ff2489f974202778ab8f596b232d0d9 7622 ocaml/lib/ocaml/stdlib__Ephemeron.cmi
9e6f193b427a6634102553c1cf7af4f903f6a84127b1aba1204379c7b14a34cf 10597 ocaml/lib/ocaml/stdlib__Ephemeron.cmx
71b981b69806270f8c584d82fa07e7f8b2bee4cda33f15dfdcb351cdbd8f8517 1367 ocaml/lib/ocaml/stdlib__Filename.cmi
6f13981bfeccc513a0a117e85b535a4078abf8cb62564421a50501fb9bb7b597 6129 ocaml/lib/ocaml/stdlib__Filename.cmx
9dde7af53e41c46b32c5a3aba6995537887403fbcd1fc7591f50962acf1574e6 10235 ocaml/lib/ocaml/stdlib__Float.cmi
4bc86f3bc236c0384fc3e86ced13c95fada1ad7e352a5f71ba645e4f680b89df 8824 ocaml/lib/ocaml/stdlib__Float.cmx
e40a08b28f296d9adbee8e7d67efceb924314a6d4baa6f39eb5348103e1b4c2d 9650 ocaml/lib/ocaml/stdlib__Format.cmi
efeff0a7797845b71e36b91b72bd3c92862997fe856d259a252fd03ff5403b6f 24903 ocaml/lib/ocaml/stdlib__Format.cmx
2e041a7e12d83756f7a376281d6a2592386ad142529fabf3d9c9be6d02736d1c 699 ocaml/lib/ocaml/stdlib__Fun.cmi
922945a9719f550e1e67ae9f4551d379b61d445345540a2fdd37153dd5699314 1009 ocaml/lib/ocaml/stdlib__Fun.cmx
039134a86964f0decce8f8190893195915b6933c80eaaef90e4c139f645bd02f 3887 ocaml/lib/ocaml/stdlib__Gc.cmi
55bd9446aebfb5093e19cde780ec28c3d43483f69373f95780e72d00be8e21b0 3081 ocaml/lib/ocaml/stdlib__Gc.cmx
75c3a0b6e0ddeeffffc63049f495bca34afe81bde21169c21ed5c503b9a6551f 7395 ocaml/lib/ocaml/stdlib__Hashtbl.cmi
8f8a6dc697788400fac54320e45e8caae42525cce921965effa3f56688de7d58 6579 ocaml/lib/ocaml/stdlib__Hashtbl.cmx
7132d1448d101007d45e15343ab4d2f2062899f1fdd5df2a5b988caad3b58536 2760 ocaml/lib/ocaml/stdlib__Iarray.cmi
e1c7e0c1455e759a092d7467ee8c9c7f3681174cdfd4e446abc18f63d783aab3 3628 ocaml/lib/ocaml/stdlib__Iarray.cmx
8bba502ab92abd8765f395fe950a9f2cd0d7ac549639482df43127d995042d78 1994 ocaml/lib/ocaml/stdlib__In_channel.cmi
6c3c6c376a839d26ac4c4db16bad340f2262635d4278ce068ef80c5696815818 2982 ocaml/lib/ocaml/stdlib__In_channel.cmx
28030efcadd55f0f794ffdfa2293c71f6acf55ac0b2cf005ff6829ff72ffe76b 1815 ocaml/lib/ocaml/stdlib__Int.cmi
dfd4bf011833da66ac63e3b5f98d456f6fa811135845f4b77e35bfd0ccd0d032 2116 ocaml/lib/ocaml/stdlib__Int.cmx
e93b765b2b8002c1597a8fd5248353181754b19e824a55b9da6e429a8f243c5c 2397 ocaml/lib/ocaml/stdlib__Int32.cmi
fa7d58cdfe4f9bbf922d5a7d1aba38ae281bab94d53f5d6f30e63ecc9ed4b8c8 3685 ocaml/lib/ocaml/stdlib__Int32.cmx
3b1daca139b9c3caa1efe8d6f0b8d2ba6855ec401dc7c7298216221f6cb125cc 2589 ocaml/lib/ocaml/stdlib__Int64.cmi
5211dec4f709b21924d057055707c6530d2598ffd34394206b9652e6541104ad 3500 ocaml/lib/ocaml/stdlib__Int64.cmx
7b93500273b089587a2dd8610c46bc022bb52082e4aecab009213d9a4f1874eb 1016 ocaml/lib/ocaml/stdlib__Lazy.cmi
c7887246992d351889841f42d7b8d2673c49b67a2c224ec5f0a657ce126ed461 1188 ocaml/lib/ocaml/stdlib__Lazy.cmx
d4a3eb85c01905a8d29afcbc7a32c1e4d74b3e9ac94320268a0d93ab876132fb 2103 ocaml/lib/ocaml/stdlib__Lexing.cmi
a0af4f7af8a6af8814d04e7ea26f91c648728dba153a7e2807c79a36a5dd804b 3524 ocaml/lib/ocaml/stdlib__Lexing.cmx
6a16f13a8ceeff9d2a64c15ef013f9d0ec422d8a8e0849c7534f025274714a52 4455 ocaml/lib/ocaml/stdlib__List.cmi
f2c7a6fa8de0fde939297c4508c42b86ec9c390e180c7fb31345a90c19174302 5234 ocaml/lib/ocaml/stdlib__List.cmx
722c473410cac521b4e017afa5c85fa02d449360a8c434f64d308e0c3c4f7db2 4535 ocaml/lib/ocaml/stdlib__ListLabels.cmi
3157752d0089ca5ce424744a32fa47d943384ab06805121c9ff59aa6de3ca59c 5039 ocaml/lib/ocaml/stdlib__ListLabels.cmx
f459ccf75a2d8f63e7f4ec0079d9585ac7014c913dd120cce6be90afc86bac30 5295 ocaml/lib/ocaml/stdlib__Map.cmi
ec7836c6a5b394d482712031f1bf5d993ec82b55b4586318b6b745bfd7028338 2965 ocaml/lib/ocaml/stdlib__Map.cmx
2f449a60f60928c260d6a85aed8aff6d78163df4d6dce8bc8f3a86a57ad41cd3 1004 ocaml/lib/ocaml/stdlib__Marshal.cmi
785ad571325d3d4862fada30b9fc75813b939975ee408a09a43a6d2a7e77abfe 1075 ocaml/lib/ocaml/stdlib__Marshal.cmx
a2080668d45cb0f2768d679fbe6810989efe1ba55d10aa90da793a6b934ce082 16903 ocaml/lib/ocaml/stdlib__MoreLabels.cmi
db6e8e0eb0ffe1327433392f808f6b8b7738a0b7f11b04ab627e3f9e09304dd4 11392 ocaml/lib/ocaml/stdlib__MoreLabels.cmx
1f6a566ddfd595d4d40227a911a77aed0a724feb2ad5fe834f83bd7739215bab 533 ocaml/lib/ocaml/stdlib__Mutex.cmi
a1394a9fbaf3edab060e256f8b8551a60ed2f54e7db9dad7dc7fc6b61fae6ec2 545 ocaml/lib/ocaml/stdlib__Mutex.cmx
64c68f12d2c956eb28fec27322243b70c91a1e199dde94f0b1554e6c3d11cbf8 2388 ocaml/lib/ocaml/stdlib__Nativeint.cmi
211357628c1bf3acdba0d78b5ea45e919830c62a6df1e8aa17ce9b3072a87d3c 4414 ocaml/lib/ocaml/stdlib__Nativeint.cmx
b310a36b9f69c273b27587079e9ee6930379d903ac6ea51dc43e2dcdfd2c1487 2698 ocaml/lib/ocaml/stdlib__Obj.cmi
b31d6c81e0e876652ce31795e8d900135617f8b0194cec353b705282f6573e67 2515 ocaml/lib/ocaml/stdlib__Obj.cmx
f859bfd93c3675fbc6e429b2dd97f63242b99f0f8c67da49c5e9bd1fe2ab3e3e 748 ocaml/lib/ocaml/stdlib__Oo.cmi
19fd49804dc46f9ae1bc740e7433ee236b0f1258cc4fcbf3be8bcdb79353342e 401 ocaml/lib/ocaml/stdlib__Oo.cmx
5bf042becd432fd3bc3d5b79f691b567bb2a9eac72a3301249120104aac9c941 1799 ocaml/lib/ocaml/stdlib__Option.cmi
e7a24c59471b1af9ddd6c416e9a7a5cec68744dcc9210ad66d23203ccb90fae8 2826 ocaml/lib/ocaml/stdlib__Option.cmx
9f1f62df7d6f04a500f68d0825b26d1f2cd524c5cac37bb65e3183ecb9b3accd 1917 ocaml/lib/ocaml/stdlib__Out_channel.cmi
c7f065730151ded2a1622d51779a9c0182759a40de064c9bf1d56ebc890ddcb4 2810 ocaml/lib/ocaml/stdlib__Out_channel.cmx
2cc418086963b45191f015f0edb519c66957af12e7415efe3c104ef4c793a1a8 1080 ocaml/lib/ocaml/stdlib__Pair.cmi
e06607c2d1aeff137d68513f05c383ca423f8066d40a0f3f5ab39b02f738cb2a 1025 ocaml/lib/ocaml/stdlib__Pair.cmx
1c347d8cac6d04c4f2af40464fa3838feb6d2ece6cd779740b252b6cb8a8f2cb 1634 ocaml/lib/ocaml/stdlib__Parsing.cmi
830264b7ce1edcf021f482c1612dd7830ee6ee194519871cde29e416f8a6dbed 2128 ocaml/lib/ocaml/stdlib__Parsing.cmx
595aa48cd161a933b3c78fb2721ab12e697cf81267da1f4258bc811be1e7294d 6313 ocaml/lib/ocaml/stdlib__Pqueue.cmi
dad0294e6d2d707445a3f62501cac571281ea14e197a82d19928316e8cd185f2 2328 ocaml/lib/ocaml/stdlib__Pqueue.cmx
326520978502ad6ae4fdbf0cd263a2c79ce7b050e4052f2faa969658f6b147bf 2436 ocaml/lib/ocaml/stdlib__Printexc.cmi
c45ed05f24d89c945490f5fd2d06980db10bc48954b77c975508876ddf246ad0 4958 ocaml/lib/ocaml/stdlib__Printexc.cmx
38d198f5ebe2d00af568fcf67ad9ee50e5a7372fea01fb2af0ea076ea36a6a93 1967 ocaml/lib/ocaml/stdlib__Printf.cmi
bd20bedd9f3abf7b80e05b86dcb35a5c8b7bce88b31563c3994a8b2a09788f1e 2332 ocaml/lib/ocaml/stdlib__Printf.cmx
9f34c973ab314932b25a76ff1ee46e6d8b7dc13e01a0cb29b0fce263a5aae6bb 1379 ocaml/lib/ocaml/stdlib__Queue.cmi
2a7e489692ae7d4838519ae030f47b423c137bc62fbee43585da68cc27598e86 1799 ocaml/lib/ocaml/stdlib__Queue.cmx
36a6283c29ff7186213eea248ca7d4cee8d1eb40daf966d9b056d2ce22932f23 2184 ocaml/lib/ocaml/stdlib__Random.cmi
f82f98ac6dd5b03cd615acd8d09a7d563003ab123b02a582ccde2352b01297ee 5555 ocaml/lib/ocaml/stdlib__Random.cmx
85f052d17dcb4dca4b829d8e10ca7858451b064d328792d02a27b5475c42a11f 526 ocaml/lib/ocaml/stdlib__Repr.cmi
7f7d6b41b49d8c3752af4caf27c2530959bc23e854694b2684518432e04ce355 256 ocaml/lib/ocaml/stdlib__Repr.cmx
636c25c72d8dc6ea84b64d303fb0d4ea7f464a0f1022529dccbb3420149df20c 2117 ocaml/lib/ocaml/stdlib__Result.cmi
5f04440b6fe5a5a1a58f9c8a86a4e944cb8a6fae9afff8f3e400200ac5659a46 3112 ocaml/lib/ocaml/stdlib__Result.cmx
75af59c6debd7c58212a6326582b01b6a4aa63b4439d660e284ab02638b69f5b 2013 ocaml/lib/ocaml/stdlib__Scanf.cmi
e114007dddc48b73b3669c48dc897bf1d9b7e6ee83b3c35e11c98922f9af7a78 28858 ocaml/lib/ocaml/stdlib__Scanf.cmx
c15b0d633a2eb4d263c55f61791ac9663fa7d3f49aa431a9942808133cebc2b1 763 ocaml/lib/ocaml/stdlib__Semaphore.cmi
60c58815694aae051f558be6fd9ee118c948455f584b4eb9e0eadde38e02d0e5 902 ocaml/lib/ocaml/stdlib__Semaphore.cmx
bf30ba6f72748cf8d19adac910c59bada56583cd9c00963ef407a3655449ac16 4037 ocaml/lib/ocaml/stdlib__Seq.cmi
007efc77bcc2b5db3b77886ecc8bbb9261be56d825933b661cf8f02e83c9f9a2 7948 ocaml/lib/ocaml/stdlib__Seq.cmx
12b22a47c705d8daa8e9eda891a7727863f6cd8e2232b0e7a91116f9e2392a80 3998 ocaml/lib/ocaml/stdlib__Set.cmi
7381acbe7b1647337e9f3eab8f9e2de7ce8031fa80303e725286a404cd7bd520 3115 ocaml/lib/ocaml/stdlib__Set.cmx
adc1da971d11a8c13d7f0af5bf57c2d07c5d0de8f018ef7ad520fff6155569cf 1240 ocaml/lib/ocaml/stdlib__Stack.cmi
028d6b17f18d651a7809f74c28b88c52d6f61500a48387e331b567750742788c 2247 ocaml/lib/ocaml/stdlib__Stack.cmx
a1b40a2c84bdadce58d85332a1aec79df1013e660dd24ab204565ca0dbca004f 383 ocaml/lib/ocaml/stdlib__StdLabels.cmi
cc2982cba7e68bc4ae385b46d02d633385bec771a3942166e089956af7005f76 182 ocaml/lib/ocaml/stdlib__StdLabels.cmx
f9950cb1c283dfb68f506a5c79844677d158cdd0602e1f9969498cd54600bfe7 5238 ocaml/lib/ocaml/stdlib__String.cmi
ebfe58878df4ed0e34d706c2baf5a956c013844782c7ae229ee769f2b1cea13e 16689 ocaml/lib/ocaml/stdlib__String.cmx
1cc39b1d904cd064f35ca4145334324b308d49b0cb9191c0dfd7f3c401995b10 5322 ocaml/lib/ocaml/stdlib__StringLabels.cmi
85cb2b532a3719147a2afd119506c3de7e0bef03c4a223ff0f2a3e90d01ea127 14343 ocaml/lib/ocaml/stdlib__StringLabels.cmx
9b593a36d4c4297ff1e73eb12b5f088dc822e3e91de179c87406ff3a4788354c 4182 ocaml/lib/ocaml/stdlib__Sys.cmi
88b2c1bd9acc1bcaac6de0288ed1ce5877aa49e155b8e27012318feb4a5c11db 1113 ocaml/lib/ocaml/stdlib__Sys.cmx
b90c36a7c8f302afdd0ad768b3ebb4f675390043f832adf669db42443e9cbe4b 621 ocaml/lib/ocaml/stdlib__Type.cmi
4decc28670d91177a3d031f6b1dcb813bce8a5a9627bf90ff6d59e7057781ee9 909 ocaml/lib/ocaml/stdlib__Type.cmx
0e2fa433d3e40d23ed7cfe4bef0ab95366c012148cadade70b9d22cac968725b 1330 ocaml/lib/ocaml/stdlib__Uchar.cmi
27f4435d82c240e444fa4bf200f1e7cfdb2a6afd545f2ced30c11e650a0a9596 2738 ocaml/lib/ocaml/stdlib__Uchar.cmx
41ab453003eece1d18a0e980c47c162e3726ddeaf226983956adc4a24421a4ca 492 ocaml/lib/ocaml/stdlib__Unit.cmi
4c88206fb4e51d6ea4f70a01e843b08de964f9ae3fb759b6d870615c1fbb476c 378 ocaml/lib/ocaml/stdlib__Unit.cmx
36eb40eae3b08d5973bd13935a2432e0a960b64a26f6f550d16a210957fc4adc 2118 ocaml/lib/ocaml/stdlib__Weak.cmi
f99ab81f847da71f0b77425eca32e8eede4708d59ea1eec471168c655546bbf5 1651 ocaml/lib/ocaml/stdlib__Weak.cmx
"""
LINK_INPUT_LOCK = """\
3ff8197f6cba257e1895499474bf66f87710a0d5657aa048a7fb76080b22379e 7827 msys64/mingw64/lib/crt2u.o
9af5e18f01a63a7d02ba11e097324e046f778de5c74cd093b52296f8613dbcc8 892 msys64/mingw64/lib/default-manifest.o
b61d8cef207fe4928c44d91ad722d15c53b9ae32a26fb69f05ace4287e887905 854 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/crtbegin.o
c3c2b8de9ec26db0994f669680d4aadad3639fc970e96f858ac0a6cc9515bde3 1037 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/crtend.o
3bf27ff273d71b177ace7b12396a71b53bb813f763f67b3140166df1f9bb90b1 3030766 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/libgcc.a
39fca07029d79f075cecda5ae1aed6dd901d2439da544506eea2040f517eff71 11726 msys64/mingw64/lib/gcc/x86_64-w64-mingw32/16.2.0/libgcc_eh.a
0b7d185a8041c052ffdf554df7636d40c950f37f5b38c852b59846badb980036 694266 msys64/mingw64/lib/libadvapi32.a
a0906d87ca3c7bceb571f5de5fd44b6f6c571d2600ae8c70fb006ad651700198 1391318 msys64/mingw64/lib/libkernel32.a
dd2c318b763fd2fabcd75a586ca885969b51a3c380f443f0621594dfe514f149 49228 msys64/mingw64/lib/libmingw32.a
0556de4387429c199d23bad432ac0e0d8cde3f498444f5a797fcc34f8076da68 554720 msys64/mingw64/lib/libmingwex.a
277843f78458aaaeb5f844e665d8fde609a816c6452685c42ab1d4359b4bedd0 1406866 msys64/mingw64/lib/libmsvcrt.a
d534cf659aa953b4ac91bc06aeafdb18ed2778b3dfc7b5effd74c0137ed3ca15 415942 msys64/mingw64/lib/libole32.a
a035b2e3befbc0f8fe5e5cec46ac7c5a8911b170f1972fad503f49f7fc8176d6 105498 msys64/mingw64/lib/libpthread.a
34bf7214ecb79c5fa18f394addce2faaa1d2f48633ab4f84074c2dbb3a4b1eed 109754 msys64/mingw64/lib/libpthread.dll.a
0d705833bbd1000f50bea5bc2cf44326acb37b308eeb23fc5fc33d77f142c85d 306742 msys64/mingw64/lib/libshell32.a
9901073289f7444d6aac89812e2c09f708e5815e81b96894db4895d27da84684 351080 msys64/mingw64/lib/libshlwapi.a
c37bef5df02fc380d48edc48fd9d01b2d2d8af4f09f9986d7afaf6275450c639 15894 msys64/mingw64/lib/libsynchronization.a
9f3a8229b0e108546b8f998da7bbce5be0e355be24fced095b7bb68295988012 756526 msys64/mingw64/lib/libuser32.a
f26ff2e17a4fa8e7f4af279d5bbd893093e3566d9a9125c70dd4faa266efdd5f 1310732 msys64/mingw64/lib/libuuid.a
ed7602f4a8695bbe12f984447e123f1c42353345c11757111441d52c4237ca3a 16370 msys64/mingw64/lib/libversion.a
5effebc2f1a703d3ded721522cba4feb263994780386fdf86f7e94f51e2b9562 191432 msys64/mingw64/lib/libws2_32.a
f09fb5f2479d7e3b5b2bde6fb56fffea1cd395b4428808c71e0be553d7079dfa 13066 ocaml/lib/ocaml/flexdll/flexdll_mingw64.o
ab3b764192045a6fc47a515075706a72a8a8f6104c684c0ff6f4e71a2a0a08d2 2617716 ocaml/lib/ocaml/libasmrun.a
e74bf777fef384dcc9a18ac4cb124a48856029d7ae633c25a66e0bfee41db781 1206 ocaml/lib/ocaml/std_exit.o
3c38289120ce777e0d4a4b5c45ac01deb4f6830c8c2cfd75411e1c310660ddb0 2240832 ocaml/lib/ocaml/stdlib.a
"""

# SHA-256, byte count and staged name from the sealed R2 build inputs.
SOURCE_LOCK = """\
f8aa0e2845a1712859d1baaa14aab913cf6b4b524d40543b828ef02d6de1724d 11700 arithmetic.ml
cdbf18be1806be2e50fcfeb575233fe06893e75db4c7682ef9c03162e76b87fc 513 arithmetic.mli
c35451f392516c3f2dcd7832576215ad5d707d8f4eb776be01bfadc7a76a1ba0 8863 core.ml
dac13608a6a0b91d8a0d38e9742892ae2ed30155a9e01b73a7143ea2dba89827 1068 core.mli
944e4cdef6987bd2a55145f722265eb5705ae2dbb2fb57241f6ef697ae9d0145 12811 driver.ml
f39875cd5a956851497e1fc5c5574d7c722ff8623f013f5652276f10913a4110 1717 json.ml
cda11498f299a470c2d23fe5567a3dd8984096f37f1d133f82ab1402ba89173c 844 json.mli
98a5e9e351832bf4c72604ff39e2f9c1aba363751692e3144ee3d40aaad06f79 5923 nat.ml
744b4a11bdedbcef8fcdf7a82fabd8bd966676e77c3ffcffddc768e15d4882e2 1810 nat.mli
73f51f28ec35d170e4ef0505344fe803da02985421d414df673363ae00c05893 3976 resolved_graph.ml
15f6014c123501a54d386c5a9a916dfa78dad7920a332ad9b111a8d78937db62 718 resolved_graph.mli
"""
SWITCH_LOCKS = {
    "regular": "bd8948790a6c99566a96d0114e68ba1f6ec059140086735cdd3b69fa395f30e1 20 probe_switch.ml",
    "probe": "05b67a35f726d9433beb5747d5e01ac5a0d28f75a0204e3b3fe069f8f59cc2dd 19 probe_switch.ml",
}

# Sealed R2 output identities as (byte count, SHA-256). None selects all runs.
REFERENCE_IMAGES = {
    "regular": (3970924, "c6f7411dd411962cd7d46e43d32293518a5fe78a2eb84a887167cfb735255120"),
    "probe": (3974402, "be45ee3b8308c154863f5ecf44547290eb707ffd03971045606e80129a49837e"),
}
REFERENCE_RECORDS = {
    None: (188182, "7134001b89cdfa34838427d224f06ea224096e6227d7d3bdb4d22a3c74360b50"),
    "ordinary": (87324, "1a33ba3d699e6c5abe05ba5555417006841e83a5105cfb0059ed6f23ebf772d1"),
    "trial-exact": (100858, "bb08244da1062286d407840d7cb2cd9a20dfe35fb890825d4a3e6f80eab0bc92"),
}
REFERENCE_DIAGNOSTICS = {
    "regular": dict.fromkeys(REFERENCE_RECORDS, (
        0, "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    )),
    "probe": {
        None: (355078, "62b6c6bc9b91c35f9a4a20cc97cd904a858fb3f0f075fab8ce2e9e84dad2960f"),
        "ordinary": (175397, "b4e08a00be5e787297027e1fc9dfbb09f4b76c0a964b87c50095ade67ddcde6e"),
        "trial-exact": (179681, "990ff7dfa739bc8137fdd29ad325ecc9adda3b122e80b1f89fda1452d3ebc127"),
    },
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def binding(path, name):
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while block := stream.read(65536):
            digest.update(block)
            size += len(block)
    return {"path": name, "bytes": size, "sha256": digest.hexdigest()}


def expected_binding(name, identity):
    size, digest = identity
    return {"path": name, "bytes": size, "sha256": digest}


def save_json(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=True)
        stream.write("\n")


def existing_directory(path):
    resolved = path.resolve(strict=True)
    if not resolved.is_dir():
        raise ValueError(f"not a directory: {path}")
    return resolved


def fresh_output(path, *protected):
    out = path.resolve()
    if any(out.is_relative_to(folder) for folder in (HERE, *protected)):
        raise ValueError(f"output must be separate from the installed tree and inputs: {out}")
    out.mkdir()
    return out


def lock_entries(table, count):
    entries = {}
    for row in table.splitlines():
        digest, size, name = row.split(" ", 2)
        path = Path(name)
        if (path.anchor or ".." in path.parts or path.as_posix() != name or path in entries
                or not re.fullmatch(r"[0-9a-f]{64}", digest) or not size.isascii()
                or not size.isdecimal()):
            raise ValueError(f"invalid lock row: {row}")
        entries[path] = {"path": name, "bytes": int(size), "sha256": digest}
    if len(entries) != count:
        raise ValueError(f"expected {count} lock rows, got {len(entries)}")
    return entries


def verify_inputs(root, entries):
    paths = {}
    for relative, expected in entries.items():
        path = (root / relative).resolve(strict=True)
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f"invalid distribution input: {relative}")
        if path.stat().st_size != expected["bytes"] or binding(path, expected["path"]) != expected:
            raise ValueError(f"distribution input differs from lock: {relative}")
        # Preserve every locked name, including aliases of the same executable.
        paths[root / relative] = expected
    return paths


def environment(root, temp, *, compile_native=False):
    system = Path(os.environ["SystemRoot"])
    search = [root / MINGW / "bin", system / "System32", system]
    env = {
        "SystemRoot": str(system),
        "WINDIR": str(system),
        "COMSPEC": str(system / "System32/cmd.exe"),
        "TEMP": str(temp),
        "TMP": str(temp),
        "SOURCE_DATE_EPOCH": "0",
        "LC_ALL": "C",
        "PYTHONUTF8": "1",
    }
    if compile_native:
        search.insert(0, root / OCAML_BIN)
        env["OCAMLLIB"] = str(root / STDLIB)
    env["PATH"] = os.pathsep.join(map(str, search))
    return env


class BuildSteps:
    def __init__(self, out, env):
        self.out = out
        self.env = env
        self.logs = out / "logs"
        self.logs.mkdir()
        self.lock = Lock()
        self.active = 0
        self.peak_jobs = 0
        self.commands = []

    def run(self, label, *arguments):
        argv = list(map(str, arguments))
        log = self.logs / (label + ".log")
        summary = {
            "step": label, "argv": argv, "started": datetime.now(timezone.utc).isoformat(),
        }
        start = time.monotonic()
        with log.open("xb") as stream:
            with self.lock:
                process = subprocess.Popen(argv, cwd=self.out, env=self.env, stdin=subprocess.DEVNULL,
                                           stdout=stream, stderr=subprocess.STDOUT)
                self.commands.append(summary)
                self.active += 1
                self.peak_jobs = max(self.peak_jobs, self.active)
            try:
                code = process.wait()
            finally:
                with self.lock:
                    self.active -= 1
        if log.stat().st_size > LOG_LIMIT:
            raise ValueError(f"build log size cap reached: {log}")
        summary.update(exit=code, seconds=time.monotonic() - start,
                       log=binding(log, log.relative_to(self.out).as_posix()))
        if code:
            raise ValueError(f"{label} exited {code}. See {log}")
        return log


def stage_sources(out, probe):
    names = sorted([f"{module}.ml" for module in MODULES]
                   + [f"{module}.mli" for module in INTERFACES])
    for name in names:
        if name == "probe_switch.ml":
            data = b"let enabled = true\n" if probe else b"let enabled = false\n"
        else:
            data = (HERE / "src" / name).read_bytes()
        (out / name).write_bytes(data)
    return names


def prerequisites(names, report):
    edges = {}
    for line in report.splitlines():
        name, colon, words = line.partition(":")
        if not colon or name not in names or name in edges:
            raise ValueError(f"unexpected ocamldep output: {line}")
        imports = set()
        for word in words.split():
            module = word[0].lower() + word[1:]
            if module in MODULES and module != Path(name).stem:
                interface = module + ".mli"
                imports.add(interface if name.endswith(".mli") and interface in names else module + ".ml")
        if name + "i" in names:
            imports.add(name + "i")
        edges[name] = imports
    if set(edges) != set(names):
        raise ValueError("ocamldep did not report every source")
    return edges


def compile_files(steps, opt, edges, jobs):
    done = set()
    running = {}
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        while edges or running:
            for name in sorted(edges):
                if len(running) == jobs:
                    break
                if edges[name] <= done:
                    task = pool.submit(steps.run, "compile-" + name, opt, *COMPILE_FLAGS, name)
                    running[task] = name
                    del edges[name]
            if not running:
                raise ValueError(f"dependency cycle involving {', '.join(sorted(edges))}")
            finished, _ = wait(running, return_when=FIRST_COMPLETED)
            for task in finished:
                task.result()
                done.add(running.pop(task))


def trace_inputs(log, out, temp, expected):
    local_objects = {out / (module + ".o") for module in MODULES}
    external = set()
    trace = []
    with log.open(encoding="utf-8") as stream:
        for line in stream:
            # GCC also prints an indented collect2 command ending in an object path.
            name = line.strip()
            if line[:1].isspace() and re.match(
                r'^"?[^"]*?collect2\.exe(?:"|\s)\s*-plugin\b', name, re.IGNORECASE
            ):
                continue
            if name.startswith("+ "):
                continue
            name = name.strip('"')
            if not name.lower().endswith((".o", ".a")):
                continue
            path = (out / name).resolve()
            trace.append(str(path))
            if path in local_objects:
                continue
            if path.parent == temp and re.fullmatch(r"(camlstartup|dyndll)[0-9a-f]+\.o", path.name):
                continue
            external.add(path)
    missing = set(expected) - external
    extra = external - set(expected)
    if extra or missing:
        raise ValueError(f"GNU ld trace differs from link lock. Missing={sorted(map(str, missing))}, "
                         f"extra={sorted(map(str, extra))}")
    for path in external:
        file = expected[path]
        if binding(path, file["path"]) != file:
            raise ValueError(f"link input changed during build: {path}")
    return trace


def verify_pe(executable):
    with executable.open("rb") as stream:
        if stream.read(2) != b"MZ":
            raise ValueError("expected a Windows executable")
        stream.seek(0x3C)
        stream.seek(int.from_bytes(stream.read(4), "little"))
        header = stream.read(12)
    if header[:4] != b"PE\0\0" or header[8:12] != bytes(4):
        raise ValueError("expected a PE image with zero COFF timestamp")


def build(args):
    root = existing_directory(args.toolchain)
    toolchain = verify_inputs(root, lock_entries(TOOLCHAIN_LOCK, 191))
    link_inputs = verify_inputs(root, lock_entries(LINK_INPUT_LOCK, 25))
    profile = "probe" if args.probe else "regular"
    expected_sources = lock_entries(SOURCE_LOCK + SWITCH_LOCKS[profile], 12)
    reference_sources = [expected_sources[path] for path in sorted(expected_sources, key=Path.as_posix)]
    out = fresh_output(args.out, root)
    receipt_path = out / "build.json"
    names = stage_sources(out, args.probe)
    source_inputs = [binding(out / name, name) for name in names]
    receipt = {
        "profile": profile,
        "runner": binding(HERE / "run.py", "run.py"),
        "toolchain_root": str(root),
        "toolchain": list(toolchain.values()),
        "link_inputs": list(link_inputs.values()),
        "source_inputs": source_inputs,
        "reference_source_inputs": reference_sources,
        "matches_reference_sources": source_inputs == reference_sources,
        "commands": [],
    }
    if not receipt["matches_reference_sources"]:
        save_json(receipt_path, receipt)
        raise ValueError(f"staged sources differ from the lock. See {receipt_path}")

    temp = out / "tmp"
    temp.mkdir()
    env = environment(root, temp, compile_native=True)
    steps = BuildSteps(out, env)
    opt = root / OPT
    steps.run("config", opt, "-config")
    steps.run("gcc-version", root / GCC, "--version")
    deps = steps.run("dependencies", root / DEP, "-modules", *names)
    jobs = min(os.cpu_count() or 1, len(names))
    compile_files(steps, opt, prerequisites(names, deps.read_text(encoding="utf-8")), jobs)
    modules = [module + ".cmx" for module in MODULES]
    log = steps.run("link", opt, *LINK_FLAGS, "-o", "evaluator.exe", *modules)
    trace = trace_inputs(log, out, temp, {path.resolve(): entry for path, entry in link_inputs.items()})
    executable = out / "evaluator.exe"
    image = binding(executable, executable.name)
    reference_image = expected_binding(executable.name, REFERENCE_IMAGES[profile])
    receipt.update({
        "executable": image,
        "reference_executable": reference_image,
        "reference_executable_sha256": reference_image["sha256"],
        "matches_reference_executable": image == reference_image,
        "link_trace": trace,
        "link_order": modules,
        "compile_flags": list(COMPILE_FLAGS),
        "link_flags": list(LINK_FLAGS),
        "max_jobs": jobs,
        "peak_jobs": steps.peak_jobs,
        "environment": env,
        "commands": steps.commands,
    })
    if receipt["matches_reference_executable"]:
        verify_pe(executable)
        receipt["coff_timestamp"] = 0
    save_json(receipt_path, receipt)
    if not receipt["matches_reference_executable"]:
        raise ValueError(f"built evaluator differs from the {profile} reference. See {receipt_path}")
    print(receipt_path)


def fixture_arguments(inputs):
    def load(name):
        name = Path(name)
        relative = name.as_posix()
        if relative not in inputs:
            path = (HERE / name).resolve(strict=True)
            if not path.is_relative_to(HERE):
                raise ValueError(f"fixture outside installed tree: {name}")
            data = path.read_bytes()
            inputs[relative] = (data, {"path": relative, "bytes": len(data), "sha256": sha256(data)})
        return inputs[relative]

    graphs = {}
    for name in sorted((HERE / "graphs").glob("*.json")):
        raw, file = load(name.relative_to(HERE))
        graphs[file["sha256"]] = raw
    descriptors = {}
    for edition, scope in (("add", "serial-root"), ("sub", "root")):
        _, descriptor = load(edition + "-descriptor.json")
        descriptors[edition] = descriptor["sha256"]
        starts = json.loads(load(edition + "-graph-starts.json")[0])
        if starts["descriptor_sha256"] != descriptor["sha256"]:
            raise ValueError(f"{edition} graph starts bind a different descriptor")
        for start in starts["starts"]:
            scheduled = start["scheduled_graph_sha256"]
            offered_bytes, offered = load(start["graph"])
            handles = [start.get("input_handle", ""), start.get("admission_handle", "i1")]
            if not all(isinstance(handle, str) for handle in handles):
                raise ValueError(f"{start['case']} uses a non-string handle")
            yield (
                start["case"], start["observers"], descriptor["sha256"], scheduled, offered["sha256"],
                "graph", start["admitted_natural"], *map(str, start["grant"]), "normal",
                graphs[scheduled].hex(), offered_bytes.hex(), start.get("scope", scope), *handles,
            )

    for edition in ("add", "sub"):
        starts = json.loads(load(edition + "-obtained-starts.json")[0])
        for start in starts:
            canonical = json.dumps(start, sort_keys=True, separators=(",", ":")) + "\n"
            digest = sha256(canonical.encode("utf-8"))
            events = start["events"]
            arguments = [start.get("selected", events[-1]["site"])]
            for event in events:
                flag = event["interrupt"]
                if flag is True:
                    marker = "interrupt"
                elif flag is False:
                    marker = "none"
                else:
                    marker = "unsupported"
                arguments.extend([event["site"], event["op"], event["left"], event["right"], marker])
            yield (
                start["case"], OBSERVERS, descriptors[edition], digest, digest,
                "obtained", "0", *map(str, start["grant"]), "normal", *arguments,
            )


def read_stream(stream, name):
    stream.seek(0)
    data = stream.read(STREAM_LIMIT + 1)
    if len(data) > STREAM_LIMIT:
        raise ValueError(f"{name} exceeded the per-run byte limit")
    return data


def run(args):
    build_dir = existing_directory(args.build)
    manifest_path = build_dir / "build.json"
    manifest = json.loads(manifest_path.read_bytes())
    profile = manifest["profile"]
    exe = build_dir / "evaluator.exe"
    image = binding(exe, exe.name)
    if profile not in REFERENCE_IMAGES:
        raise ValueError(f"unknown build profile: {profile}")
    reference_image = expected_binding(exe.name, REFERENCE_IMAGES[profile])
    receipt = {
        "profile": profile,
        "observer": args.observer,
        "runner": binding(HERE / "run.py", "run.py"),
        "build": binding(manifest_path, "build.json"),
        "executable": image,
        "reference_executable": reference_image,
        "matches_reference_executable": image == reference_image,
    }
    toolchain_path = Path(manifest["toolchain_root"])
    if not receipt["matches_reference_executable"] or image != manifest.get("executable"):
        out = fresh_output(args.out, build_dir, toolchain_path.resolve())
        receipt_path = out / "capture.json"
        receipt["build_executable"] = manifest.get("executable")
        receipt["runs"] = []
        save_json(receipt_path, receipt)
        if not receipt["matches_reference_executable"]:
            raise ValueError(f"evaluator differs from the {profile} reference. See {receipt_path}")
        raise ValueError(f"evaluator does not match the build receipt. See {receipt_path}")
    root = existing_directory(toolchain_path)
    runtime_dlls = {
        path: file for path, file in lock_entries(TOOLCHAIN_LOCK, 191).items()
        if path.parent == MINGW / "bin" and path.suffix.lower() == ".dll"
    }
    verify_inputs(root, runtime_dlls)

    fixtures = {}
    plan = [
        (name + "/" + observer, [str(exe), name, observer, *arguments])
        for name, allowed, *arguments in fixture_arguments(fixtures)
        for observer in allowed
        if args.observer is None or args.observer == observer
    ]
    expected_runs = 94 if args.observer is None else 47
    if len(plan) != expected_runs or len({name for name, _ in plan}) != expected_runs:
        raise ValueError(f"expected {expected_runs} distinct fixture runs")
    out = fresh_output(args.out, build_dir, root)
    env = environment(root, out)
    runs = []
    counts = Counter()
    diagnostic_count = 0
    capture_error = None
    with (out / "records.jsonl").open("xb") as records, (out / "diagnostic.jsonl").open("xb") as diagnostics:
        for name, argv in plan:
            with tempfile.TemporaryFile(dir=out) as stdout, tempfile.TemporaryFile(dir=out) as stderr:
                result = subprocess.run(argv, cwd=out, env=env, stdin=subprocess.DEVNULL,
                                        stdout=stdout, stderr=stderr, timeout=12, check=False)
                canonical = read_stream(stdout, name + " stdout")
                diagnostic = read_stream(stderr, name + " stderr")
            records.write(canonical)
            diagnostics.write(diagnostic)
            by_kind = Counter()
            if result.returncode:
                capture_error = f"{name} exited {result.returncode}"
            elif profile == "regular" and diagnostic:
                capture_error = f"{name} emitted unexpected stderr"
            else:
                try:
                    by_kind = Counter(json.loads(line)["kind"] for line in canonical.splitlines())
                except (ValueError, KeyError, TypeError) as error:
                    capture_error = f"{name} emitted invalid canonical records: {error}"
            side_count = len(diagnostic.splitlines())
            counts.update(by_kind)
            diagnostic_count += side_count
            runs.append({
                "run": name,
                "argv": argv,
                "exit": result.returncode,
                "counts": dict(by_kind),
                "canonical_sha256": sha256(canonical),
                "canonical_bytes": len(canonical),
                "diagnostic_sha256": sha256(diagnostic),
                "diagnostic_bytes": len(diagnostic),
                "diagnostic_lines": side_count,
            })
            if capture_error:
                break
    records_file = binding(out / "records.jsonl", "records.jsonl")
    diagnostic_file = binding(out / "diagnostic.jsonl", "diagnostic.jsonl")
    reference_records = expected_binding("records.jsonl", REFERENCE_RECORDS[args.observer])
    reference_diagnostic = expected_binding("diagnostic.jsonl", REFERENCE_DIAGNOSTICS[profile][args.observer])
    receipt.update({
        "fixtures": [file for _, file in fixtures.values()],
        "records": records_file,
        "diagnostic": diagnostic_file,
        "reference_records": reference_records,
        "reference_records_sha256": reference_records["sha256"],
        "matches_reference_records": records_file == reference_records,
        "reference_diagnostic": reference_diagnostic,
        "matches_reference_diagnostic": diagnostic_file == reference_diagnostic,
        "counts": dict(counts),
        "diagnostic_lines": diagnostic_count,
        "runs": runs,
    })
    receipt_path = out / "capture.json"
    save_json(receipt_path, receipt)
    if capture_error:
        raise ValueError(f"{capture_error}. See {receipt_path} and {out / 'diagnostic.jsonl'}")
    if not (receipt["matches_reference_records"] and receipt["matches_reference_diagnostic"]):
        raise ValueError(f"capture differs from the reference. See {receipt_path}")
    print(receipt_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    builder = commands.add_parser("build", help="build in a fresh output directory")
    builder.add_argument("--toolchain", type=Path, required=True)
    builder.add_argument("--out", type=Path, required=True)
    builder.add_argument("--probe", action="store_true", help="enable stderr diagnostics")
    runner = commands.add_parser("run", help="capture the installed fixtures in a fresh directory")
    runner.add_argument("--build", type=Path, required=True)
    runner.add_argument("--out", type=Path, required=True)
    runner.add_argument("--observer", choices=OBSERVERS, help="select one observer")
    args = parser.parse_args()
    try:
        if os.name != "nt":
            raise ValueError("the recorded toolchain requires Windows")
        if args.command == "build":
            build(args)
        else:
            run(args)
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        parser.exit(1, f"{parser.prog}: {error}\n")


if __name__ == "__main__":
    main()
