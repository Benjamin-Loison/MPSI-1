type 'a file = {mutable avant: 'a list; mutable arriere: 'a list};;
exception Vide;;

(* 1 2 3 4 5 6 7 8 9 10 11 12 13 *)

(* ex *)
let f = {avant = [1; 3]; arriere = [12; 0; 8]};;

let nouv_file() = {avant = []; arriere = []};; (* OK *)

let est_vide file = file.avant = [] && file.arriere = [];;

let premier file =
	if file.avant = [] && file.arriere = [] then raise Vide;
	if file.avant = [] then List.hd (List.rev file.arriere)
	else List.hd file.avant;;

(* Prof *)
let premier f = match f with
| f when est_vide f -> raise Vide
| f when f.avant = [] -> List.hd (List.rev f.arriere)
| f -> List.hd (f.avant);;

(* List.tl/hd sur livre vide fait planter *)

let retire file =
	if file.avant = [] && file.arriere = [] then raise Vide;
	if file.avant = [] then 
	let a = List.hd file.avant in
		file.avant <- List.tl file.avant;
		a;;

let retire file = match file.avant with
[] -> (
			match List.rev file.arriere with
      	[] -> raise Vide
      	| a::b -> file.avant <- b; file.arriere <- []; a (* on met de la seconde dans la première afin d'améliorer la complexité car par la suite on pourra piocher directement dans la 1ère au lieu de reverse la 2nde... *)
      )
| a::b -> file.avant <- b; a;;

(* DS: peut faire récursif même si pas indiqué sur le sujet *)
(* teacher *)

let retire f = match f.avant with
| t::q -> f.avant <- q; t
| [] -> match List.rev f.arriere with


let a = nouv_file();;
ajoute a 2;;
ajoute a 3;;
a;;
retire a;;

let ajoute file element = file.arriere <- file.arriere@[element];;

List.rev[];; (* works, works, works *)
List.rev([]);;
List.rev [];;

(* Nop, teacher: *)

let ajoute f x = f.arriere <- x::f.arriere;;

let f = nouv_file();;
for i = 1 to 10 do
	ajout f i done;;
f;;

let longueur file = List.length file.avant + List.length file.arriere;;

type 'a arbre = Vide | Noeud of ('a arbre) * 'a * ('a arbre);;

let feuille x = Noeud (Vide, x, Vide);;
let arbre = Noeud (feuille 1, 3, Vide);;

let mafonction a = match a with
| Vide -> ...
| Noeud (g, x, d) -> ... ;;

let rec taille a = match a with
Noeud (g, x, d) -> 1 + taille g + taille d
| _ -> 0;;

(* prof *)

let rec taille a = match a with
Vide -> 0
| N(g, _, d) -> 1 + (taille g) + (taille d);;

taille arbre;;
(* taille arbre vide: 0
hauteur arbre vide = 0
hauteur arbre qu'avec racine = 0*)

let rec hauteur a = match a with
Noeud (g, x, d) -> 1 + max (hauteur g) (hauteur d)
| Vide -> -1;;

hauteur arbre;;
hauteur Vide;;
hauteur feuille 2;;

(* $T(n) = O(1) + T(n_g) + T(n_d)$ on parle d'induction structurelle on est donc bien en linéaire aussi pour la hauteur*)

(* pas en grand O, on est en theta, linéaire en la hauteur de l'arbre *)
let rec maxval a = match a with
Vide -> failwith "arbre vide"
| Noeud (Vide, x, Vide) -> x
| Noeud (Vide, x, d) -> max x (maxval d)
| Noeud (g, x, Vide) -> max (maxval g) x
| Noeud (g, x, d) -> max (max (maxval g) (maxval d)) x;;(* attention à l'ordre ! *)

min_int;;
max_int;;
min_float;;
max_float;;

maxval arbre;;

let rec recherche a x = match a with
Noeud(g, e, d) when x > e -> recherche d x (* Noeud(g, x, d) = étiquette renommé en x (bullshit) *)
| Noeud(g, e, d) when x = e -> true
| Noeud(g, e, d) when x < e -> recherche g x
| _ -> false;;
(* complexité linéaire en la hauteur de l'arbre *)

(* arbre appelé peigne:

3
 *
  *
   *
    *

si équilibré: log n (sinon rien gagné si peigne ?)

*)

(* teacher *)

let rec recherche a x = when a with
Vide -> false
| Noeud(g, e, d) when e = x -> true
| Noeud(g, e, _) when e > x -> recherche g x
| Noeud(_, e, d) -> recherche d x;;

(* prof *)

let rec maxval a = match a with
| Vide -> failwith "Vide"
| Noeud(g, e, Vide) -> e
| Noeud(_, _, d) -> maxval d;;

recherche arbre 2;;
recherche arbre 1;;
recherche arbre 3;;
recherche arbre 4;;

(*

le max c'est l'élement qui n'a pas de branche droite (ce n'est pas forcément une feuille, exemple):

3
1 10
 6
4 8


3
1 8
  6 10
 4 9

n'est pas un ABR (exemple 8)

verif si un arbre est un ABR, pas juste comparer gauche et droite

*)

let rec ajoute a x = match a with
| Noeud(g, e, Vide) when e < x -> (*Noeud(g, e, feuille x)*)
| Noeud(Vide, e, d) when e > x -> (*Noeud(feuille x, e, d)*)
| Noeud(g, e, d) when e < x -> ajoute d e
| Noeud(g, e, d) when e > x -> ajoute g e
| _ -> ();;

let suppr_max a = ;;

let supprime a = ;;

(* faute de base: bang et vecteur/liste (indice) *)
(* fautes: même type match (sortie) 
| [] -> ...
| [a] -> ... USELESS
| t::q -> 

récursif: peut faire appel à une fonction récursive
si pas récursif alors que marqué récursif -> 0
de même respecté la signature
filtrage pas forcément récursif et inversement

*)