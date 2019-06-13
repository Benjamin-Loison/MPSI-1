(* on somme les valeurs du tableau T supérieurs à m et on renvoie cette valeur divisée par le nombre
d'éléments que l'on y a ajouté *)

let moyMin t m =
	let sum = ref 0. and counter = ref 0. in
		for i = 0 to ((Array.length t) - 1) do
			if t.(i) >= m then
			(
				sum := !sum +. t.(i);
				counter := !counter +. 1.;
			)
		done;
	!sum /. !counter;;

moyMin [|1.; 2.; 5.; 7.; 2.|] 4.;;

(* let moyMin t m = 0;; *)

let myList = [1; 2; 3];;
let myArray = [|1; 2; 3|];;

let rec listLength l =
	match l with
	| [] -> 0
	| t::q -> 1 + listLength q;;

let rec nieme l n = match l with
| t::q when n = 1 -> t
| t::q when n > 1 -> nieme q (n - 1)
| _ -> failwith "pas de nieme";;

listLength [1; 2; 3];;
listLength [];;
listLength [1];;

(* on définit précédemment la fonction listLength et nieme tout en faisant attention de prendre le minimum pour le maximum des indices des lignes et des colonnes*)
let fillMatrix l n = 
	let mat = Array.make_matrix n n 0 in
		let minIndex = min (listLength l - 1) (n - 1) in 
			for i = 0 to (n - 1) do
				for j = 0 to minIndex do
					mat.(i).(j) <- nieme l (j + 1);
				done;
			done;
	mat;;

let str = "MPSI 2";;
str.[4] <- "a";;
str.[1] <- 'l';;

let matrice l n =
	let m = Array.make_matrix n n 0 in
		let rec aux i j l =
			if i > n-1 || l = [] then ()
			else if j > n-1 then aux (i+1) 0 l
			else (m.(i).(j) <- List.hd l;
					aux i (j+1) (List.tl l))
	in aux 0 0 l ;
	m;;

fillMatrix [1; 2; 3] 5;;
matrice [1; 2; 3] 5;;
fillMatrix [1; 2; 3] 2;;
matrice [1; 2; 3] 2;;

let fact n =
	let res = ref 1 and m = ref n in
		while !m > 0 do
			res := !res * !m; decr m
		done; !res;;

let echange t i j =
	let c = t.(i) in
		t.(i) <- t.(j);
		t.(j) <- c;;
		
let drapeau t =
	let n = Array.length t in
		let a = ref 0 and b = ref 0 and c = ref (n - 1) in
			while !a + !b <= !c do
				match t.(!a + !b) with
				| 0 -> incr b
				| -1 -> echange t (!a + !b) (!a);
				        incr a
				| 1 -> echange t (!a + !b) !c;
				decr c;
			done;
		t;;

drapeau [|1; -1; 0; -1; 1|];;

let rec nonterm n =
	if n != 0 then
	(
	    nonterm (n - 1);
		 print_string " ";
		 print_int n
	);;

nonterm 10;;

let rec terminale n =
	if n != 0 then
	(
		print_int n;
		print_string " ";
		terminale (n - 1)
	);; (* ex: 4 *)

terminale 10;;

let term n =
	let rec aux p q =
		if p <= q then
		(
			print_int p;
			print_string " ";
			aux (p + 1) q
		)
	in aux 1 n;;

term 10;;

let rec fibo n = match n with
| 0 | 1 -> n
| _ -> fibo (n - 2) + fibo (n - 1);;

fibo 0;;
fibo 1;;
fibo 2;;
fibo 3;;
fibo 4;;

let fiboterm n =
	let rec aux (x, y) n = match n with
	| 1 -> y
	| n -> aux (y, x + y) (n - 1)
in aux (0, 1) n;;

fiboterm 0;; (* don't work anymore in this version *)
fiboterm 1;;
fiboterm 2;;
fiboterm 3;;
fiboterm 4;;

let contient v e =
	let n = Array.length v in
		let trouve = ref (v.(0) = e) and i = ref 0 in
			while not !trouve && !i <n do
				trouve := v.(!i) = e;
				incr i
			done;
	!trouve;;

let vectinter v w =
	let u = [||] in
		for i = 0 to (Array.length v - 1) do
			if not contient u v.(i) then let u = (* *);;

let s = "mpsi";;
s.[0] <- 'M';;
s;;

type point = {x: float; y: float};;
let p1 = {x = 2.; y = 3.};;
p1.x <- 2.42;; (* doesn't work *)

type point = {mutable x: float; mutable y: float};;
let p1 = {x = 2.; y = 3.};;
(* modifier un champ: *)
p1.x <- 1.5;; (* par exemple *)

let milieu a b = {x = (a.x +. b.x) /. 2.; y = a.y +. b.y /. 2.};;

type('a, 'b) couple = {x: 'a; y: 'b};;
let test = {x = "cold"; y = 75};;
(* test: (string * int) *)

type point= {mutable x: float; mutable y: float};;
type vect = {dx: float; dy: float};;

let translation p v = 
	p.x <- p.x +. v.dx;
	p.y <- p.y +. v.dy;;

type reeletendu = Reel of float | Plusinfini | Moinsinfini;;

let pi = Reel 3.14;;
let etendu_of_float x = Reel x;;

let logetendu x = match x with
| x when x = Reel 0. -> Moinsinfini
| Plusinfini -> Plusinfini
| Reel x when x > 0. -> Reel (log x)
| _ -> failwith "x est négatif";;

let addition r s = match (r, s) with 
| Reel x, Reel y -> Reel (x +. y)
| Moinsinfini, Reel x -> Moinsinfini
| Plusinfini, Reel x -> Plusinfini
| Reel x, Plusinfini -> Plusinfini
| Reel x, Moinsinfini -> Moinsinfini
| a, b when a = b -> a
| _ -> failwith "non défini";;

let div a b = 
	if b = 0 then raise "Error" else a /. b;;
	
exception trouvee;;

(* let len n =
	(int_of_float (log (float_of_int n))) + 1;;

len 0;;
len 1;;
len 27;;
len 485;;

let digit n i = *)

let len n =
	let nTmp = ref n and l = ref 1 in
		while !nTmp >= 10 do
			nTmp := !nTmp / 10;
			incr l;
		done;
	!l;;

let rec puissance x n =
	match n with
	| 0 -> 1
	| _ -> x * puissance x (n - 1);;

puissance 2 2;;
puissance 2 3;;

let subInt n i =
	let p = puissance 10 (i) in
		(n mod (p * 10)) / p;;

subInt 47 0;;
subInt 47 1;;
subInt 47 2;;
subInt 4 0;;
subInt 4 1;;
subInt 471 0;;
subInt 471 1;;
subInt 471 2;;
subInt 471 3;;

len 0;;
len 1;;
len 9;;
len 10;;
len 11;;
len 21;;
len 99;;
len 100;;
len 101;;

let isArmstrong n =
	let sum = ref 0 in
		for i = 0 to len n - 1 do
			sum := !sum + (puissance (subInt n i) 3);
		done;
	!sum = n;;

(* on énumère de façon exhaustive les nombres de 0 à n et on vérifie le caractère d'Armstrong en utilisant des fonctions travaillant de façon arithmétique pour obtenir les chiffres du nombre *)
let armstrong n =
	for i = 0 to n do
		if isArmstrong i then
		(
			print_int i;
			print_newline();
		)
	done;;

armstrong 1000;;

let cube x = x * x * x ;;
let rec somme_cube_chiffres = function
| 0 -> 0
| n -> cube (n mod 10) + somme_cube_chiffres (n / 10) ;;

let armstrong n =
	let l = ref [] in
		for i = 0 to n do
			if i = somme_cube_chiffres i then
			l := i::(!l);
		done;
	!l ;;

(* on considère que l'entrée est différente d'un tableau vide *)
let indicePlateauMaximal t =
	let maxTmp = ref 1 and max = ref 1 and maxIndice = ref 0 in
		for i = 1 to Array.length t - 1 do
			if t.(i) == t.(i - 1) then
			(
				incr maxTmp;
				if(!maxTmp > !max) then
				(
					max := !maxTmp;
					maxIndice := i - !max + 1;
				)
			)
			else
				maxTmp := 1;
		done;
	!maxIndice;;

indicePlateauMaximal [1; 1; 2; 2; 2; 3; 3; 4; 4; 4; 4; 5; 5; 6; 6 ;7 ];;

let indicePlateauMaximal l =
	let rec aux l = match l with
		| [] -> (0, 0, 0)
		| [a] -> (1, 0, 1)
		| t::q -> let (lm, im, l0) = aux q in
			if t<>List.hd(q) then (lm, im + 1, 1)
			else let l0Prime = l0 + 1 in
				if l0Prime > lm then (l0Prime, 0, l0Prime)
				else (lm, im + 1, l0Prime)
	in let (l1, i1, l2) = aux l in i1 ;;

let addPrevEl l0 e =
	let l = Array.length l0 in
		let l1 = Array.make (l + 1) 0 in
			l1.(0) <- e;
			for i = 0 to (l - 1) do
				l1.(i + 1) <- l0.(i)
			done;
	l1;;

addPrevEl [||] 1;;
addPrevEl [| 1; 2; 3 |] 4;;

List.length [1; 2; 3];;

let arrayRev l0 =
	let l = Array.length l0 in
		let l1 = Array.make l 0 in
			for i = 0 to l - 1 do
				l1.(i) <- l0.(l - i - 1);
			done;
	l1;;

arrayRev [|1; 2; 3|];;

let is2Palin n =
	let l = ref [||] in
		let quotient = ref n in
			while !quotient != 0 do
			(
				l := addPrevEl !l (!quotient mod 2);
				quotient := !quotient / 2;
			)
			done;
	let bool = ref true in
		let len = Array.length !l in
			for i = 0 to (len - 1) / 2 do
				if !l.(i) != !l.(len - i - 1) then
				(
					bool := false;
				)
			done;
	!bool;;

let miror t =
	let rec aux t l =
		match t with
		| [||]
		| t.(i) != t.() false;
	in aux t Array.length l;;

let is2Palin n =
	let t = ref [||] in
		let quotient = ref n in
			while !quotient != 0 do
			(
				t := addPrevEl !t (!quotient mod 2);
				quotient := !quotient / 2;
			)
			done;
	let l = Array.length !t and i = ref 0 in
		while !i < n / 2 && !t.(!i) = !t.(l - 1 - !i) do
			incr i
		done;
	!i = (n / 2);;

is2Palin 3;;
is2Palin 5;;
is2Palin 9;;
is2Palin 42;;

let rec base_2 n =
if n <= 1 then [n] else (n mod 2)::base_2 (n/2) ;;

let palindrome n = let a = base_2 n in a = (List.rev a) ;;

let test l =
	match l with
	| a::b::c -> print_int 2
	| a::b -> print_int 1
	| _ -> print_int 0;;

test [];; (* 0 *)
test [1];; (* 1 *)
test [1; 2];; (* 2 *)

let rec check l i =
	match l with
	| [] | [_] when i = 0 -> true
	| a::b::q when i = 1 && a <= b -> check (b::q) (i - 1)
	| a::b::q when a < b -> check (b::q) (i + 1)
	| _ -> false;;

(* assume liste vide non donnée en entrée *)
let isConvenable l =
	let len = listLength l in
		if (len mod 2) = 0 then
		(
			let bool = ref true in
				let i = ref 1 in
					while !bool && !i < len do
						if (!i mod 2) = 1 then if l.(!i - 1) > l.(!i) then bool := false
						else if l.(!i - 1) >= l.(!i) then bool := false;
						incr i;
					done;
				bool;
		)
		else false;;

let isConvenable l =
	if l = [] then true
	else check l 1;;

isConvenable [];;
isConvenable [1];;
isConvenable [1; 1];;
isConvenable [1; 1; 1];;
isConvenable [1; 1; 1; 1];;
isConvenable [1; 1; 2; 2];;
isConvenable [1; 1; 2; 1];;

List.hd [1; 2; 3];;
List.tl [1; 2; 3];;
List.length [1; 2; 3];;
[1; 2; 3].(0);; (* doesn't work *)
[1; 2; 3].[0];; (* too *)
[|1; 2; 3|].(0);;

let debug l1 =
	match l1 with
	| a::b::c -> print_int a; print_string " "; print_int b
	| _ -> print_string "aba";;

debug [];;
debug [1];;
debug [1; 2];;
debug [1; 2; 3];;

let rec test l1 l2 =
	match l1, l2 with
	| a::b::c, d::e::f when b < d -> test c f
		| a::b::c, d::e::f when b = d -> 4@test c f
	| _ -> [];;

let rec inter l1 l2 =
	match l1, l2 with
	| a::b::c, d::e::f when b < d -> inter c (d::e::f)
	| a::b::c, d::e::f when e < a -> inter (a::b::c) f
	| a::b::c, d::e::f -> [max a d]@[min b e]@(inter c f) (* [] are important ! parenthesis isn't enough *)
	| _, _ -> [];;

(* no capito: Warning 8: this pattern-matching is not exhaustive.
Here is an example of a case that is not matched:
((_::_::_, _::[])|(_::_::_, [])|(_::[], _)|([], _)) *)

let intersection l1 l2 =
	inter ;;

let rec intersection l1 l2 = match (l1,l2) with
| ([],_) -> []
| (_,[]) -> []
| (a::b::q,c::d::r) -> let e = max a c and f = min b d in
let l3 = if b > f then (max (f+1) a)::b::q else q in
let l4 = if d > f then (max (f+1) c)::d::r else r in
if e > f then intersection l3 l4
else e::f::intersection l3 l4 ;;

intersection [2; 4] [1; 3];;
intersection [8; 8] [7; 7];;
intersection [8; 8] [8; 8];;
intersection [-3; -2; -1; 2; 4; 7; 8; 8] [-10; 20];;
intersection [-3; -2; -1; 2; 4; 7; 8; 8] [-3; -2; -1; 2; 4; 7; 8; 8];;
intersection [-3; -2; -1; 2; 4; 7; 8; 8] [-1; 0; 1; 3; 4; 6; 7; 8];;

test [2; 4] [1; 3];;

let union l1 l2 =
	;;

let rec union l1 l2 =
match (l1,l2) with
([],_) -> l2
|(_,[]) -> l1
|(a::b::q,c::d::r) ->
if b<c then a::b::union q l2
else if d<a then c::d::union l1 r
else union (a::d::q) r ;;

let fill l n =
	let mat = Array.make_matrix n n 0 in
		let rec aux i j l =
			if i > n - 1 || l = [] then ()
			else if j > n - 1 then (aux (i + 1) 0 l)
			else mat.(i)
		aux 0 0 l;
	mat;;

let cube x = x*x*x;;

let rec somme_cube_chiffres n =
	match n with
	| 0 -> 0
	| n -> cube (n mod 10) + somme_cube_chiffres (n / 10);;

let armstrong n =
	let l = ref [] in
		for i = 0 to n - 1 do
			if (somme_cube_chiffres i) = i then (l := i::(!l))
		done;
	!l;;

armstrong 1000;;

let rec base2 n =
	if n <= 1 then [n]
	else (n mod 2)::(base2 (n / 2));;

base2 2;;
base2 8;;

let indicePlateauMaximal ;;

let rec aux l i j n =
	if l = [] then n
	else if (List.hd l) = (i, j) || (List.hd l) = (j, i) then aux (List.tl l) i j (n + 1)
	else aux (List.tl l) i j n;;
aux reseau.liens;;

let rec aux l i j =
	if l = [] then false
	else if (List.hd l) = (i, j) || (List.hd l) = (j, i) then true
	else aux (List.tl l) i j;;

let declare_amis res i j =
	if not (aux res.liens i j) then res.liens <- res.liens::(i, j);;

List.hd [1; 2; 3];;
List.hd [];;

let liste_amis res i =
	let rec aux l i n =
		if l = [] then n
		else (match (List.hd l) with
		| (i, _) | (_, i) -> aux (List.tl l) i (n + 1)
		| (_, _) -> aux (List.tl l) i n);;
	
let test = 42;;

if test <> 41 then print_int 0 else print_int 1;;