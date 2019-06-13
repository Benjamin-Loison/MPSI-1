def somme(n):
    sum = 0
    for k in range(1, n + 1):
        sum += ((-1) ** k) / k
    return sum


print([i for i in range(10)])

for i in range(10):
    print(i)

from math import pi, sqrt

def absolute(x):
    if x < 0:
        return -x
    return x

def meilleure_approximation():
    u = 2
    uBest = u
    smallest = u
    n = 1
    nBest = n
    power2 = 0
    while u != 0:
        abso = absolute(2 ** power2 *  - pi)
        if smallest > abso:
            smallest = abso
            uBest = u
            nBest = n
        u = sqrt(2 - sqrt(4 - u ** 2))
        n += 1
        print(abso, u, pi)
    return uBest, nBest

print(meilleure_approximation())

def carre_parfait(n):
    
def pythagicien(n):
    for c+ in range 

myList = [1, 2, 3]
myList[1] = [4, 3]
print(myList)
del(myList[0])
print(myList * 2)
print(2 * myList)

(2, 3.0)

list(42) # doesn't work

if True:
    bcd = "a"
else:
    bcd = "e"
print(bcd)

TVA = 2

def sum(a, b):
    TVA = 1
    return (a + b) * TVA

print(sum(1, 2), TVA)

print((0,))

for i, j in zip((1, 2), (3, 2, 1)):
    print(i, j)

a = 2
b = 3
c = 4
print(id(a))
print(id(b))
print(id(c))
print(type(id(a)))

def sum(*terms):
    print(len(terms))

sum(a, b)

f = open('C:/Users/Benjamin LOISON/Desktop/test.txt', 'r')
for line in f.readlines():
    print(line)
print(list(f.read(10)))
print(f.read(1))
print(type(f.read(10)))
print(type(f.read(1)))
f.seek(0)
print(bytes(f.read(10)))

c = f.read(1)
while c:
    c = f.read(1)
    print(c)

c = f.read(1)
while c != b'':
    c = f.read(1)
    print(c)

octet = b''
print(octet == True)

print(bytes(range(256)))
print(bytes(range(256))[0])

for i in range(10):
    print(bytes(1)[0][i])
    
print(list(enumerate(range(5))))

a = [1, 2, 3]
a[2:2] = [4]
print(a)

L = [1, 2, 3]
L2 = [0]
L3 = L2
L2 += L
print(L3, L2)
L3[0] = -1
print(L2)

for i in range(, 10, 2): # doesn't work
    print(i)

