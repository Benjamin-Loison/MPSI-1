let rec egypt p q = match p with
| 0 -> 0
| p when p mod 2 = 0 -> egypt (p / 2) (q * 2)
| _ -> egypt (p / 2) (2 * q) + q;;

egypt 2 3;;
egypt 4 5;;
egypt 6 7;;
egypt 8 9;;

5 / 2;;

let rec soudan n x y = match n, y with
| (0, _) -> x + y
| (_, 0) -> x
| _ -> let p = soudan n x (y - 1) in soudan (n - 1) p (p + y);; (* verified *)

(*

	N²
	x <= N² y
	x = (x1, x2)
	y = (y1, y2)
	x <= N² y si x1 <= y1 et x2 <= y2

*)

let rec palindrome s =
	let rec aux i j = match (i, j) with
	| i, j when i >= j -> true
	| i, j -> s.[i] = s.[j] && aux (i + 1) (j - 1)
	in aux 0 (String.length s - 1);;

palindrome "";;
palindrome "a";;
palindrome "aa";;
palindrome "ab";;
palindrome "aaa";;
palindrome "baab";;
palindrome "cbaabc";;

palindrome "kayak";;
palindrome "cbaabe";;
palindrome "cbdabc";;

(* let rec ackerman m n = match (m, n) with
| (0, n) when n > 0 -> ackerman 0 (n - 1)
| (m, n) when m >= 1 && n >= 1 ->  ackerman (m - 1) (ackerman m (n - 1))
| (m, 0) when m >= 1 -> ackerman (m - 1) 1;; wrong *)

let rec ack m n = match (m, n) with
| 0, _ -> n + 1
| _, 0 -> ack (n - 1) 1
| _ -> ack (n - 1) (ack n (n - 1));;

(* pas plutôt ? *)

let rec ack m n = match (m, n) with
| 0, _ -> n + 1
| _, 0 -> ack (m - 1) 1
| _ -> ack (m - 1) (ack m (n - 1));;





ackerman 3 4;;

(*

	A0(n) = n + 1
	A1(0) = A0(1) = 2
	A1(n) = A0(A1(n - 1)) = 1+A1(n - 1)

*)