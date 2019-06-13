fun f x y -> f x y;;
fun f g x -> g (f x);;
nop ('a -> 'b -> 'c) -> ('a -> 'c) -> 'b -> 'c;;

fun x -> 1+ (x + 1);;

fst (1, 2);;

List.map (fun x -> x * x) [1; 2; 3];;

fst [|1; 2|];;