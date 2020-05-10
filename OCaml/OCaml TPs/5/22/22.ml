(* complexité linéaire *)
let rec applique f l = (* List.map *)
	match l with
	[] -> l
	| a::b -> f a::(applique f b);;

let f x = x * x;;

applique f [0; 1; 2; 3];;

(* linéaire en la taille de la première liste *)
let rec concat l1 l2 =
	match l1 with
	[] -> l2
	| t1::q1 -> t1::(concat q1 l2);;


(* B *)
let rec concat l1 l2 = (* @ *)
	match l2 with
	[] -> l1 (* case [a] is useless because is in the next *)
	| a::b -> concat (l1::a) b;;

concat [1; 2; 3] [4; 5; 6];;

List.length [1; 2; 3];;
(* List.sublist [1; 2; 3] 2;; doesn't work *)

(* let est_sous_liste m1 m2 =
	let i = ref 0 in
		let l1 = List.length m1 in
			let l2 = List.length m2 in
				while i < l2 - l1 do
					let j = ref 0;
					while j < i + l1 do
						
						incr j;
					done;
					incr i;
				done; *)

let rec est_sous_liste m1 m2 =
	match m1, m2 with
	[], _ -> true
	| _, [] -> false
	| a::b, c::d when a = c -> est_sous_liste b d
	| a::b, c::d -> est_sous_liste (a::b) d;;

est_sous_liste [1; 3; 2] [0; 1; 3; 4; 2];;
est_sous_liste [7; 3; 2] [0; 1; 3; 4; 2];;

(* on admet sigma(m) = ... *)

(* B *)
let sous_listes m = (* return liste de listes *)
	let res = ref [] in
		let rec aux m =
			let sq = (sous_listes q) in
				match m with
				[] -> 
				| t::q -> (sous_listes q)@(t::sq)
		in aux m;;

(* correc *)
let rec sousliste l = match l with
| [] -> [[]]
| t::q -> let sigma = sousliste q in concat sigma (applique (fun x -> t::x) sigma);; (* appliqe/concat *)

sousliste [1; 2; 3; 4];;

let rec plslc m1 m2 =
	match m1, m2 with
	[], _ | _, [] -> 0 (* constante si double filtrage sur une ligne ? *)
	| t1::q1, t2::q2 -> max ((plslc q1 q2) + (if t1 = t2 then 1 else 0)) (max (plslc m1 q2) (plslc q1 m2));;

plslc [1; 2; 3] [2; 3 ;4];;

let plslc2 m m1 m2 =
	let a1 = Array.of_list m1 and a2 = Array.of_list m2 in
		let l1 = ((Array.length i) + 1) and l2 = ((Array.length j) + 1) in
			let sol = Array.make_matrix l1 l2 0 in
				for i = 1 to l1 do
					for j = 1 to l2 do
							sol.(i).(j) <- plslc a1.(i - 1) a2.(j - 1)
					done
				done;;

(* correc *)
let plslc2 m1 m2 =
	let delta x y = if x = y then 1 else 0 in
		let t1 = Array.of_list m1 and t2 = Array.of_list m2 in
			let n1 = Array.length t1 and n2 = Array.length t2 in
				let sol = Array.make_matrix (n1 + 1) (n2 + 1) 0 in
					for i = 1 to n1 do
						for j = 1 to n2 do
							(* sol.(i).(j) <- max (max (sol.(i - 2).(j - 2) + (delta (m1.(i - 1)) (m2.(j - 1)))) sol.(i - 1).(j - 2)) sol.(i - 2).(j - 1) *)
							sol.(i).(j) <- max (sol.(i - 1).(j - 1) + delta t1.(i - 1) t2.(j - 1)) (max sol.(i - 1).(j) sol.(i).(j - 1)) done; done; sol.(n1).(n2);;

(* programmation dynamique = pas de récursif (boucle for) *)

(* f(n, p) = f(n - 1, p) + f(n - 1, p - 1) + f(n, p - 1) *)

let rec count n p =
	match n, p with
	0, _ | _, 0 -> 1
	| n, p -> (count (n - 1) (p - 1)) + (count n (p - 1)) + (count (n - 1) p);;

count 5 5;;
count 10 10;;
count 20 20;;

(* 5 juin DS 2 *)
(* 12 juin tp *)

let count2 n p =
	let sol = Array.make_matrix n p 1 in
		for i = n - 1 downto 1 do
			for j = p - 1 downto 1 do
				sol.().()
			done
		done;;

(* correc *)
let fdyn n p =
	let t = Array.make_matrix (n + 1) (p + 1) 1 in
		for i = 1 to n do
			for j = 1 to p do
				t.(i).(j) <- t.(i - 1).(j - 1) + t.(i).(j - 1) + t.(i - 1).(j)
			done
		done
	t.(n).(p);;

let fdyn2 n p =
	let t = Array.make (p + 1) 1 in
		let v = ref 1 in
			for i = 1 to n do
				for j = 1 to p do
					let a = t.(j) in
						t.(j) <- t.(j - 1) + t.(j) + !v;
						v := a
				done;
				v := 1;
			done;
			t.(p);;

fdyn2 10 10;;