let l = [1; 2];;

2::l;;
l::2;; (* imp *)

let a = [|1; 2|];;
let b = Array.copy a;;
a.(0) <- 0;;
b;;
a;;

();;