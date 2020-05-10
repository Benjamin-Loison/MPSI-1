let rec hamming n = match n with| 1 -> true
| 0 -> false
| n when n mod 2 = 0 -> hamming (n / 2)
| n when n mod 3 = 0 -> hamming (n / 3)
| n when n mod 5 = 0 -> hamming (n / 5)
| _ -> false;;

hamming 1;;
hamming 0;;
hamming 2;;
hamming 4;;
hamming 6;;
hamming 8;;
hamming 11;;

print_int (7 mod 2);;

let rec somme f n = match n with
| 0 -> f 0 
| _ -> somme f (n - 1) + f n;;

let f n = n * n;;
somme f 3;;

let rec catalan n = match n with
| 0 | 1 -> 1
| _ -> let f p = (catalan p) * (catalan (n - 1 - p)) in somme f (n - 1);;
(* do not bother with illegal character *)

catalan 1;;
catalan 2;;
catalan 3;;
catalan 4;;

let rec puissance x n = match n with
| 0 -> 1
| _ -> (puissance x (n - 1)) * x;;

puissance 4 0;;
puissance 4 1;;
puissance 4 2;;
puissance 4 3;; 

let rec exprap x n = match n with
| 0 -> 1
| _ -> let p = exprap x (n / 2) in (if n mod 2 = 0 then 1 else x) * p * p;;
(* or n *)

exprap 2 3;;
exprap 3 4;;
exprap 4 5;;

let rec egypt p q = match p with
| 0 -> 0
| _ -> (egypt (p / 2) (2 * q)) + (p mod 2) * q;;
(* | p when p mod 2 = 0 -> egypt (p / 2) (2 * q) | _ -> egypt ((p - 1) / 2) (2 * q) + q;; *)

let rec egypt p q = match p with
| 0 -> 0
| p when p mod 2 = 0 -> egypt (p / 2) (2 * q)
| _ -> egypt ((p - 1) / 2) (2 * q) + q;;

egypt 2 3;;
egypt 3 4;;
egypt 5 6;;

(*
   T(n) = 1 + T(n - 1)
   T(0) = 0
*)

let f x = x * x;;

(* respect signature *)
let rec itere n f x = match n with
| 0 -> x
| _ -> f (itere (n - 1) f x);; (* fct récursive *)

(* or itere (n - 1) f (f x) différence complexité spatialle (pas temporelle) - fonction récursive terminale *)

(* correc *)
let rec itere n f x = match n with
| 1 -> f x
| _ -> f (itere (n - 1) f x);;

let a = [|1; 2; 3|];;
let b = Array.copy a;;

let c = [|1; 2.0|];;
let d = [1, 'a'];;

true & true;;