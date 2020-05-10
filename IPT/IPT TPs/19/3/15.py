from time import clock
tic = clock()
L = []
for i in range(10 ** 5): # complexité linéaire au début
    L = L + [0]
tac = clock()
print(tac - tic)
# 21.9

from time import clock
tic = clock()
L = []
for i in range(10 ** 5):
    L += [0]
tac = clock()
print(tac - tic)
# 0.014

from time import clock
tic = clock()
L = []
for i in range(10 ** 5):
    L[len(L):len(L)]= [0]
tac = clock()
print(tac - tic)
# 0.0396 (vraie différence temporelle par rapport à avant)

from time import clock
tic = clock()
L = []
for i in range(10 ** 5):
    L[len(L):]= [0]
tac = clock()
print(tac - tic)
# 0.02913