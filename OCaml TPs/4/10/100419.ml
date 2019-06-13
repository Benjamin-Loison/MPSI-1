
let rec puissance x n = match n with
| 0 -> 1
| _ -> let a = puissance x (n / 2) in (if n mod 2 = 0 then 1 else x) * a * a;;

(* let mult a b = [||];; peut faire comme ça *)

let mult a b = 
	let res = Array.make_matrix 2 2 0 in
		for i = 0 to 1 do
			for j = 0 to 1 do
				res.(i).(j) <- a.(i).(0) * b.(0).(j) + a.(i).(1) * b.(1).(j)
			done;
		done;
		res;;

let rec puissanceMat a n =
	let id = [|[|1;0|];[|0;1|]|] in match n with
	| 0 -> id
	| _ -> let b = puissanceMat a (n / 2) in (if n mod 2 = 0 then id else a) * b * b;;

let rec puissanceMat a n = match n with
	| 0 -> [|[|1;0|];[|0;1|]|]
	| _ -> let b = puissanceMat a (n / 2) in mult (if n mod 2 = 0 then [|[|1;0|];[|0;1|]|] else a) (mult b b);;

(* corrigé *)
(* n^3 complexité multiplier matrices *)
(* n^4 complexité puissance matrices *)
(* expo rap (n^3)log n *)

let rec puissmat m n = match n with
| 1 -> m
| n when n mod 2 = 0 -> let a = puissmat m (1 / 2) in mult a a
| _ -> let a = puissmat m (n / 2) in mult m (mult a a);;

let rec puissmat m n = match n with
| 1 -> [|[|1;0|];[|0;1|]|]
| n when n mod 2 = 0 -> let a = puissmat n (1 / 2) in mult a a
| _ -> let a = puissmat m (n / 2) in mult m (mult a a);;

(* end corrigé *)

(* [] lin *)

let a = [|[|1;2|];[|3;4|]|];;
let b = [|[|5;6|];[|7;8|]|];;
let c = [[|1;2|];[|3;4|]];;
let d = [|4;8;7;5;4;1|];;

puissanceMat a b;;

let res = Array.make_matrix 2 2 0;;
res.(0).(0);;
res.(0).(0) <- 2;;

let max_dicho x t =
	let rec cherche_entre i j =
		let best = ref t.(0) in
			if j < i then !best
			else if t.((i + j) / 2) > best then best := t.((i + j) / 2);
			cherche_entre i (j - (j - i) / 2) and cherche_entre (i + (j - i) / 2) j
	in cherche_entre 0 (Array.length t - 1);;

let maximum t =
	let n = Array.length t in
		maxi [| maxi (Array.sub t 0 (n/2));maxi (Array.sub t (n/2) (n/2))|];;

(* corrigé *)

let rec maximum t =
	let n = Array.length t in
	if n = 1 then t.(0) else
		let t1 = Array.sub t 0 (n/2) and t2 = Array.sub t (n/2) (n - (n/2)) in
			let a1 = maximum t1 and a2 = maximum t2 in
				max a1 a2;;

maximum d;;

(*Cn = C_\floor{n/2} + C_\ceil{n/2} + O(n)
     = O(nlog n) (pas mieux qu'algorithme naïf) *)

(* list.length linéaire *)
(* accéder élément tableau temps constant ? *)
(* longueur liste mais pas tableau *)
(* ecrire en style impératif (non récursif) une fonction maxi qui détermine le maximum dans un tableau non trié de complexité linéaire *)
let maxi t =
	let n = Array.length t in
		let max = ref t.(0) in
			for i = 1 to n - 1 do
				if t.(i) > !max then max := t.(i)
			done;
		!max;;

maxi [|4;7;53;2|];;

let n = Array.length t in
let t1 = Array.sub t 0 (n/2) in
let t2 = Array.sub t (n/2) (n - (n/2)) in
(* Array.sub linéaire en la longueur donnée *)

(* let l1, l2 = diviser l in
fusion (trif l1) (trif l2)
C_n = 2c_{n/2} + O(n) *)

let calInf n =;;
	

(* on écrit une fonction qui calcule deux suites (ip) (jp) tq \forall ip² <= n < jp²
qd j = i + 1 i est l'entier cherché *)

let sqrt n = 
	let rec cherche i j =
		let k = (i + j) / 2 in
			match k*k with
   		| _ when j = i + 1 -> i
   		| p when p < n -> cherche k j
   		| p when p = n -> k
   		| _ -> cherche i k
   	in cherche 0 (n + 1);;
  
sqrt 5;;
sqrt 10001000;;