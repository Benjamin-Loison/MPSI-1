let rec dernier l = match l with
| [] -> failwith "pas de dernier"
| [a] -> a
| t::q -> dernier q;;

dernier [1;2;3];;

let rec avantdernier l = match l with
| [a;b] -> a
| t::q -> avantdernier q
| _ -> failwith "pas d'avant dernier";;

(* or following is best *)

let rec avantdernier l = match l with
| [] | [_] -> failwith "pas d'avant dernier"
| [a;b] -> a (* or [a;_]*)
| t::q -> avantdernier q;;

break;;

let a = [|1; 2; 3|];;
a.(0);;
let b = [1; 2; 3];;
b.(0);;

avantdernier [1;2;3];;
avantdernier [1;2];;
avantdernier [1];;
avantdernier [];;

(* let rec nieme i l = match i, l with
| (_, []) -> failwith "liste pas assez longue"
| (0, _) -> l
| _ -> nieme (i - 1) t::q;; *)

let rec nieme n l = match l with
| t::q when n = 1 -> t
| t::q -> nieme (n - 1) q
| [] -> failwith "liste pas assez longue";;

(* best *)
let rec nieme n l = match l with
| t::q when n = 1 -> t
| t::q when n > 1 -> nieme (n - 1) q
| [] -> failwith "pas de nieme";;

nieme 4 [1; 2; 3];;
nieme 2 [1; 2];;
nieme 1 [1];;
nieme 0 [];;
nieme 1 [];;

[|1; 2; 3|]@[|2; 4; 5|];; (* doesn't work *)
4::[|1; 2; 3|];; (* doesn't work *)

(* linéaire en n *)
let rec listmake n e = match n with
| 0 -> []
| n when n > 0 -> e::(listmake (n - 1) e)
| _ -> failwith "n negatif";;

(* following is bullshit because too complex *)
let rec listmake n e = match n with
| 0 -> []
| n when n > 0 -> (listmake (n - 1) e) @ [e];;

listmake 2 3;;
listmake 1 3;;
listmake 0 3;;

let rec sum l = match l with
| [] -> 0
| t::q -> t + (sum q);;

sum [];;
sum [1; 2];;
sum [4; 5; 6];;

(* not max(a, b), do max a b*)

(* let rec maxlist l =
	let a = ref l.(0) in
		let rec iterate l = match l with
		| t::q when q > !a -> a := q && iterate q
		| t::q -> iterate q;
	!a;;

let l = [1; 4; 3];;
let a = ref l.(0);;
let rec iterate l = match l with
| t::q when q > !a -> a := q && iterate q
| t::q -> iterate q;;
iterate l;;
!a;; *)

(* complexité linéaire en la longueur de la liste *)
let rec maxlist l = match l with
| [] -> failwith "pas de max"
| [a] -> a
| t::q -> max t (maxlist q);;

let rec minlist l = match l with
| [] -> failwith "pas de min"
| [a] -> a
| t::q -> min t (minlist q);;

max 1 2;;
max 1. 2.;;

max [1; 2];;
max [1.; 2.];;

maxlist [1; 3; 4; 1];;
maxlist [1];;
maxlist [];;
maxlist [1.; 3.; 4.; 1.];;
maxlist ['a', 'd', 'b'];; (* nop *)
maxlist ["a", "bc", "d"];; (* nop *)

let rec minmaxlist l = match l with
| [] -> failwith "no elements"
| [a] -> [a; a]
(* not necessary | [a; b] -> [max a b; min a b]*)
| t::q -> [max t (maxlist q); min t (minlist q)];;

minmaxlist [1; 2; 3];;
minmaxlist [1; 5; 4; 2];;
minmaxlist [1; 2];;
minmaxlist [];;
minmaxlist [1];;

(* prof version *)
let rec minmax l = match l with
| [] -> failwith "liste vide"
| [a] -> (a, a)
| t::q -> let (a, b) = minmax q in (min a t, max b t);;

let test a = a == 42;;

test 0;;
test 42;;

let positif a = a >= 0.;;

positif 0.;;
positif -1.;; (* why bug ? *)

(* ('a -> bool) -> ('a list) -> bool *)
(* pefect <3 #EvaluationParesseuse *)
let rec exists testfunc l = match l with
| [] -> false
| t::q -> testfunc t || exists testfunc q;;

(* pas de complexité en O(2n), juste O(n) != nombre de concaténations que l'on fait ... *)

exists test [1; 2; 3];;
List.exists test [1; 2; 3];;
exists test [1];;
List.exists test [1];;
exists test [1; 2];;
List.exists test [1; 2];;
exists test [];;
List.exists test [];;
exists test [1; 42; 3];;
List.exists test [1; 42; 3];;

(* perfect <3 *)
let rec for_all testfunc l = match l with
| [] -> true
| t::q -> testfunc t && for_all testfunc q;;

for_all test [];;
List.for_all test [];;
for_all test [1];;
List.for_all test [1];;
for_all test [1; 2];;
List.for_all test [1; 2];;
for_all test [42; 41];;
List.for_all test [42; 41];;
for_all test [42; 42; 42];;
List.for_all test [42; 42; 42];;

let rec miroir l = match l with
| [] -> []
| t::q -> (miroir q)@[t];;
(*

T0 = 1
Tn = Tn-1 + n
Tn = n(n+1)/2 = O(n²)

*)

let test2 l =
	match l with
	| t::q -> q
	| [] -> [];;

test2 [1];; (* t::q match even if [42] is given *)

let miroirlin l =
	let rec aux acc l = match l with
	| [] -> acc
	| t::q -> aux (t::acc) q
in aux [] l;;

(*

l [2; 1]
aux [] [2; 1] acc = [] l = [2; 1]
aux 2::[] [1] acc = [2] l = [1]
aux 1::[2] [] acc = [1; 2] l = []

*)

let rec print_list = function 
[] -> ()
| e::l -> print_int e; print_string " "; print_list l;;

bothcheck miroir List.rev;;

let bothcheck f1 f2 =
	check f1; check f2;;

let checkpart func l =
	print_list(l);
	print_newline();
	print_list(func l);
	print_newline();
	print_newline();;


let check func =
	checkpart func [];
	checkpart func [0];
	checkpart func [0; 1];
	checkpart func [0; 1; 2];;

(* let rec is_croissant l = match l with
| [] | [_] -> true
| t::q -> t <= maxlist q;;

check is_croissant;; *)

let rec croiss l = match l with
| [] | [_] -> true
| a::b::q -> a <= b && croiss (b::q);;

let monotone l = croiss l || croiss (List.rev l);;(* is_décroissant: linéaire "deux fois" *)

monotone [];;
monotone [1];;
monotone [2; 1];;
monotone [1; 2];;
monotone [1; 2; 3];;
monotone [1; 2; 1; 2];;

(* let rotg l = l.(List.length l - 1) *)

let rotg l = match l with
| [] -> []
| t::q -> q@[t];;

let rotd l = List.rev (rotg (List.rev l));;

(* complexité linéaire *)

rotd [1; 2; 3];;
rotd [1; 2; 3; 4; 5];;

let rec intersection l1 l2 = (* assume sorted lists *)
	match l1, l2 with
	| l, [] | [], l -> l
	| a::p, b::q when a = b -> [a]@(intersection p q)
	| a::p, b::q (* check contains *) -> [a; b]@(intersection p q);;

intersection [] [];;
intersection [1] [];;
intersection [] [2];;
intersection [1] [2];;
intersection [] [1; 2];;
intersection [1; 2] [2];;

(* différence symétrique ? *)

let rec union l1 l2 =
	match l1, l2 with
	| l, [] | [], l -> l
	| a::p, b::q (* kind of same *);;

[1; 2; 3] = [1; 3; 2];;

let egal l1 l2 = (union l1 l2) = (intersection l1 l2);;
(* or check length of intersection with length of one of both lists *)

(* correc *)

(* B: n² + n concaténation pire cas *)
let rec intersection l1 l2 = match l1 with
| [] -> []
| t::q when List.mem t l2 -> t::(intersection q l2)
| t::q -> intersection q l2;;

(* B: n² *)
let rec union l1 l2 = match l1 with
| [] -> l2
| t::q when List.mem t l2 -> union q l2
| t::q -> t::(union q l2);;

(* B: n *)
let rec elimine a l = match l with
| [] -> []
| t::q when t = a -> q
| t::q -> t::(elimine a q);;

(* B: n^3 *)
let rec difference l1 l2 = match l2 with
| [] -> l1
| t::q when List.mem t l1 -> difference (elimine t l1) q
| t::q -> difference l1 q;; (* t@(diff ...) plutôt non ? *)

(* B: same diff *)
let rec egal l1 l2 = (difference l1 l2 = []);;