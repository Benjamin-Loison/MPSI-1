## Horner

def evaluate(sum = 0, coefficientIndex = 0):
    if coefficientIndex == coefficientsLength - 1: return sum + coefficients[coefficientIndex]
    else: return evaluate((sum + coefficients[coefficientIndex]) * x, coefficientIndex + 1)

coefficients = [4, 3, 2, 1]
x = 2

sum = coefficients[0] * x
coefficientsLength = len(coefficients)
for coefficientIndex in range(1, coefficientsLength - 1):
    print(coefficients[coefficientIndex], sum, x)
    sum = (coefficients[coefficientIndex] + sum) * x
sum += coefficients[coefficientsLength - 1]

print(sum)
print(evaluate())

    
#ax^2 + bx +c
#c+x(b + x(a))

## R1 // R2

R1 = 10
R2 = 5

def equivalentResistor(R1, R2):
    return (R1 * R2) / (R1 + R2)
    
print(equivalentResistor(10, 20))

## test

for i in range(0, .5): print(i)

int(4.6) => 4

a = 42
print(a)
a = "str"
print(a)
print(type(a))

def log():
    print("logged !")

print(False or log())

myTuple = (4, 2) 
myTuple[1] = 7

myList = [4, 2]
myList[1] = 3

for char in "abcdef": print(char)

myNewList = [0, 1, 2, 3, 4, 5, 6, 7]
print(myNewList[-2:])

print(sum([k ** 3 for k in range(1, 10)]))

print([int(k) for k in "1997"])

## Prime

import math

def isPrime(number):
    if number % 2 == 0: return False
    for potentialDivisor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % potentialDivisor == 0: return False
    return True
    
print(isPrime(97))

## Un recursive

# U(n+1) = 3 * Un + 7
# U(0) = 2

def expression(nTemporary = 0, Un = 2):
    if nTemporary == n: return Un
    return expression(nTemporary + 1, 3 * Un + 7)

n = 4
print(expression())

## Fibonacci

def fibonacci(n):
    Fn, FnPlusUn = 1, 1
    FnPlusDeux = Fn + FnPlusUn
    for k in range(n):
        Fn = FnPlusUn
        FnPlusUn = FnPlusDeux
        FnPlusDeux = Fn + FnPlusUn
    return Fn

print(fibonacci(45))

## Syracuse

def syracuse(a):
    n = 0
    while a != 1:
        if a % 2 == 0: a /= 2
        else: a = 3 * a + 1
        n += 1
    return n
    
print(syracuse(157))