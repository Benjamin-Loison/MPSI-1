let rec fusion l0 l1 = match l0, l1 with
[], l1 -> l1
| l0, [] -> l0
| t0::q0, t1::q1 when t0 < t1 -> t0::(fusion q0 l1)
| l0, t1::q1 -> t1::(fusion l0 q1);;

let rec divise l = match l with
[] -> [], []
| [a] -> [a], []
| a::b::q -> let (l0, l1) = divise q in a::l0, b::l1;;

let rec tri_fusion l = match l with
[] -> []
| [a] -> [a]
| l -> let (l0, l1) = divise l in fusion (tri_fusion l0) (tri_fusion l1);;

divise [4; 7; 5; 2; 4; 1; 5; 8];;
tri_fusion [4; 7; 5; 2; 4; 1; 5; 8];;

let inversionNumber t =
	let tMaxIndex = (Array.length t) - 1 and inversionCounter = ref 0 in
		for i = 0 to tMaxIndex do
			for j = (i + 1) to tMaxIndex do
				if t.(j) < t.(i) then incr inversionCounter;
			done;
		done;
	!inversionCounter;;

inversionNumber [|2; 3; 1; 5; 4|];;

(* doute liste/tableaux:
"on sépare le tableau en deux"
"listes triées"
*)

let scission t =
	let listIndex = ref 0 and l0 = ref [] and l1 = ref [] in
		for i = 0 to (Array.length t) - 1 do
			if !listIndex = 0 then (l0 := (!l0)::t.(i); incr listIndex)
			else (l1 := !l1::t.(i); decr listIndex)
		done;
	l0, l1;;

(* complexité en taille de t au carré (quadratique) *)

(* formule de récurrence ? *)
let rec acheval l0 l1 inversionCounter = match l0, l1 with
h0::q0, h1::q1 when h0 > h1 -> acheval q0 q1 (inversionCounter + 1)
| h0::q0, h1::q1 -> acheval 
| _, _ -> inversionCounter;;

let inversion t =
	let l0, l1 = scission t	in (* calcul inversion de façon récursive ? *)
		let rec aux l inversionCounter = match l with
			[] -> inversionCounter
			| []
		in (aux l0 0) + (aux l1 0) + (acheval l0 l1);;

(*  *)