L.append(a)
L += [a]
L[index:index] = [a]
L = L + [a] # bullshit (may recopy full list)

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 # alias (not copy initial list but takes new elements)
L1 += L2
print(L1, L3)
# [1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6]

# += ne recopie pas la liste initiale

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1
L1 = L1 + L2
print(L1, L3)
# [1, 2, 3, 4, 5, 6] [1, 2, 3]

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1
L1[len(L1):] = L2
print(L1, L3)
# [1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6]

from time import clock
tic = clock()
L = []
for i in range(10 ** 6): # complexité linéaire au début
    L = L + [0]
tac = clock()
print(tac - tic)
# 21.9

from time import clock
tic = clock()
L = []
for i in range(10 ** 6):
    L += [0] # he lives this <3
tac = clock()
print(tac - tic)
# 0.014

from time import clock
tic = clock()
L = []
for i in range(10 ** 6):
    L[len(L):len(L)]= [0]
tac = clock()
print(tac - tic)
# 0.0396 (vraie différence temporelle par rapport à avant)

from time import clock
tic = clock()
L = []
for i in range(10 ** 6):
    L[len(L):]= [0]
tac = clock()
print(tac - tic)
# 0.02913 (différence temporelle relativement non comparable sur de si petits tests)

