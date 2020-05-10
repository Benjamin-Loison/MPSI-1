for element in ["fire", "water"]:
	print("I like: " + element)
print("This will contains water: " + element)

for character in 'abc':
	print("Char: " + character)

i, j = 42, 63
print(i, j)

n = 10
square = ("& " * n + "\n") * n
print(square)

str = "azerty"
for i in range(5, -1, -1):
	print(str[i])

for i in range(10):
	print(i)
	i += 2 # (doesn't work ?)

n = 4 ## line
p = 2 ## column
matrix = [[0] * p] * n
print(matrix)

n = 10
k = 1
while k < n:
    print(k * '~ ')
    k += 1

