(*
	n = 0; 0
	n = 1; 1
	n = 2; 3
	n = 3; 6
	n = 4; 10
	n = 5; 15
*)

(* method 0 with a for loop *)

let sumNb0 n =
	let sum = ref 0 in
	for i = 0 to n do
		sum := !sum + i
	done;
	!sum;;

(* method 1 with a direct compute *)

let sumNb1 n = n * (n + 1) / 2;;

(* main *)

(* input *)

let n = 5;;

(* manual *)

(*
	print_int (sumNb0 n);
	print_newline();
	print_int (sumNb1 n);
	print_newline();
*)

(* for *)
for i = 0 to n do
	print_int (sumNb0 i);
	print_newline();
	print_int (sumNb1 i);
	print_newline();
    done;;