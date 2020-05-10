(* fact(n) impé et fonc;;*)

let rec fact n = match n with
| 1 -> 1
| _ -> n * fact (n - 1);;

fact (-1);; (* infinite *)
fact 0;; (* infinite *)
fact 1;;
fact 2;;
fact 3;;
fact(4);;

let fact n =
	let res = ref 1 in
		for i = 1 to n do
			res := !res * i;
		done;
	!res;;

let fact n =
	let res = ref 1 and i = ref 1 in
		while !i <= n do
			res := !res * !i;
			incr i;
		done;
	!res;;

sin 2.;;

5. /. 2.;;

let a = 1;;
let a = 2 in 2*a;;
a;;

let b = 1 in 2 * b;;

let a = 1 and b = 2 in a * b;;

let c = 2 and d = 2 * c in c * d;;

abs (-4);;

5 mod 2;;

log(2.7);;

sqrt(2.);;

tan(0.75);;

tanh(2.);;


-4.;;


let mul m n = m * n;;
mul (3, 2);; (* doesn't work *)


let a = [| 1; 2; 3 |];;
let b = Array.make 2 (-1);;
let c = Array.make_matrix 2 3 (-1);;

while false(*true*) do (* work without parenthesis *)
	print_endline "abc";
done;;

let disp t =
	for i = (Array.length t) - 1 downto 0 do
		print_int t.(i);
		print_newline();
	done;;

disp [|1; 2; 3|];;

print_newline();;
print_int(42);;

print_int (3 * 3);;
print_newline();;

print_float (3. ** 2.);;

print_string "1
2
3";;

print_string "1\n2\n3";;

let c = [| 4; 'a'; "str"; 4.2|];; (* doesn't work *)
let l = [4; 2; 3];;
let m = [1; 2; 4];;

List.tl l;;
m@l;;

List.mem 5 l;;

let rec dernier l = match l with
| [] -> failwith "liste vide"
| [t] -> t
| t::q -> dernier q;;

dernier [ 1; 2; 3 ];;

let a = 1073741823;;
a + 1;;
2 * a;;
5 mod 2;;
5 / 2;;
int_of_float (2.**61.);;
int_of_float (2.**62.);;
int_of_float (2.**63.);;
true & true;; (* both don't work *)
false | true;;

'a';;
"a";;

let sum (a, b) = a + b;;

let x = 5 in
	let y = 1 - x in
		x + y;;
		
let x = 7 in
	let y = 1 - x in
		x + y;;

let x = 5 and y = 1 - x in
	x + y;; (* doesn't work *)

let a = 1 in
	let a = a + 1 in
		let b = a + 1 in a + b;;

let a = 1 in
	let a = a + 1 and b = a + 1 in a + b;; (* 4 *)

let a = 2;;
let f x = a * x;;
let a = 3 in f 1;; (* 2 *)

let a = 3 and f x = a * x;;
f 1;; (* 2 *)

let a =
	let a = 3 and b = 2 in
		let a = a + b and b = a - b in
			a - b;; (* 4 *)

let b = 2 in a - b * b;; (* 0 *)

fun f x y -> f x y;;
fun f g x -> g (f x);;

let myFunc f = (f 1) + 2;;

