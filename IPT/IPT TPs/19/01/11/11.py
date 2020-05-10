def somme(*termes):
    sum = 0
    termes[0] = 42
    for terme in termes:
        sum += terme
    return sum
    
def somme(*termes): return sum(termes)

a, b, c = 1, 2, 3
sum = somme(a, b, c)
print(a, b, c, sum)

x = [1, 2, 3]
x = 'bouh'
print(x)

L = [1, 2, 3]
capsule = [42]
L = [capsule] + L
capsule[0] = 2
print(L)

L = [0, 1, 2]
capsule = [7] ; L += [capsule] ; print(L)
capsule[0] = 'bouh' ; print(L)
capsule[0] = "sobihan"
print(L)

def f(liste):
    temp = []
    for x in liste:
        temp += [x ** 2]
    return temp
    
def g(liste):
    for i in range(len(liste)):
        liste[i] **= 2
    
L = list(range(6))
f(L) ; g(L) ; print(L)

def f(nb):
    return nb ** 2
    
    
x = 10
f(x)
print(x)

def g(liste):
    liste[0] **= 2

x = [10]
g(x)
print(x)

L = [0, 1, 2]
L1 = L[:]
L[0] = "aka"
print(L, L1)

from copy import copy

L3 = copy(L1)
L3[2] = 5
print(L3, L)

L = list(range(10))
L2 = L[6 : 10] ; print(L2)

#suprimer élment par index ou valeur ?both

def delList(La, index):
    La = La[index:index] + La[index + 1:]

L = list(range(5))
print(L)
delList(L, 2)
print(L)

# delete a unique value in a list
def delByValue(La, value):
    index = -1
    for indexTmp in range(len(L)):
        if La[indexTmp] == value:
            index = indexTmp
            break
    La = La[:index] + La[index + 1:]
    print(L)
    
L = list(range(5))
print(L)
delByValue(L, 2)
print(L)

L = list(range(12))
L[6 : 10] = [10, 15]
print(L)

L[1:5] = []
print(L)

L[2:2] = [6, 7, 8, 9]
print(L)

L[:0] = [1, 2]
print(L)
L = [1, 2, 3]
L[7:7] = [42]
print(L)

L = [1, 2, 3, 4]
L2 = L + [] ; print(L2)
L[0] = 'bouh' ; print(L) ; print(L2)

L = [1, 2, 3, 4]
L2 = [0]
L3=L2
L2 = L2 + L
print(L3)

L = [1, 2, 3, 4]
L2 = [0]
L3=L2
L2 = L2 + L
L3[0] = -1
print(L2)

print()
print()
print()
print()
print()

M = [[0] * 6] * 4
print(M)

M = []
for i in range(4):
    M += [[0] * 6]
print(M)

M[3][5] = 42

M = [[0]*6 for j in range(4)]


import copy
A = copy.deepcopy(M)

print(type(zip()))

abra # <- ça crash ici (variable non définie)
def test():
    abra = 42
print(abra)
test()
print(abra)

print(type(enumerate([1, 2, 3])))
a = [0, 1]
b = [1, 2, 3]
print(list(zip(a, b)))

complément d e500 à 1000