module Make (Store : sig
  type scope
  val none : scope Value.t
  val natural : Natural.t -> scope Value.t
end) = struct
  let dispatch ~meter ~at op ~left ~right =
    let invoice = Meter.arithmetic op left right in
    let construct _ =
      match Value.as_natural left, Value.as_natural right with
      | Some x, Some y ->
          let result = match op with
            | Checker.Add -> Natural.add x y
            | Checker.Sub -> Natural.sub x y
            | Checker.Mul -> Natural.mul x y
          in
          Store.natural result
      | None, _ | Some _, None -> Store.none
    in
    Meter.pay meter ~at invoice ~build:construct
end
