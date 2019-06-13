
let rec count n p =
	match n, p with
	0, _ | _, 0 -> 1
	| n, p -> (count (n - 1) (p - 1)) + (count n (p - 1)) + (count (n - 1) p);;

count 5 5;;
count 10 10;;
count 11 11;;
count 12 12;;
count 13 13;;
count 14 14;;
count 15 15;;
count 16 16;;
count 20 20;;