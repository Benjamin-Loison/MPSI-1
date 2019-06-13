let cube = ref 0. in
let nbStr = ref "" in
let sumDigit = ref 0 in
let digit = ref 0 in

for nb = 0 to 1000 do

	cube := (float_of_int nb) ** 3.;
	nbStr := (string_of_int (int_of_float !cube));
	sumDigit := 0;

	for character = 0 to (String.length !nbStr - 1) do
		digit := int_of_char (String.get !nbStr character) - 48;
		sumDigit := (!sumDigit + !digit);
		done;
		
	if nb == !sumDigit then
		begin
		print_int nb;
		print_newline();
		end;
		
	done;