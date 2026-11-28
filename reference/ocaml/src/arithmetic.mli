val add :
  definition:string -> descriptor:string -> site:string -> interrupt:bool ->
  prepare:(Core.value -> Json.t -> Json.t) ->
  Core.account -> Core.view -> Core.value -> Core.value ->
  (Core.value, string) result * Json.t * (string * Json.t) list

val sub :
  definition:string -> descriptor:string -> site:string -> interrupt:bool ->
  prepare:(Core.value -> Json.t -> Json.t) ->
  Core.account -> Core.view -> Core.value -> Core.value ->
  (Core.value, string) result * Json.t * (string * Json.t) list
