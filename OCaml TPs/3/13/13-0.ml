let sinc x = match x with
| 0. -> 1.
| y -> (sin y) /. y;;

sinc 0.;;
sinc 2.7;;

let l = [1;2;3];;
let b = 2::l;;

let sinc x = match x with
| 0. -> 1.
| x -> (sin x) /. x;;

