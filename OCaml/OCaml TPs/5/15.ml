let solal n =
	let i = ref 0 in
		match n with
		0 -> incr i; !i
		| _ -> decr i; !i;;

solal 0;;
solal 1;;