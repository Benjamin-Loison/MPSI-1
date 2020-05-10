import matplotlib.pyplot as plt

def f(x): return x ** 2

# sinus, continue croissant: trapèze, rectangle à gauche/droite/milieu

def primitive (f, a, b, ci, n = 100): # nuage de points à primitiver # mettre en dernier argument optionnel (# on ne sait pas appeler la fonction avec le nom de l'argument)
    dx = (b - a) / n
    X = [a + k * dx for k in range(n + 1)]
    Y = [f(x) for x in X] # on veut (x^3)/3
    P = [ci]
    for i in range(n): # sum partielle des trapèzes
        P.append(P[i] + trapeze(Y[i], Y[i + 1], dx))
    #P = [trapeze() for i in range(n)] # nuage de points primitivés
    return (X, P)

def trapeze(l0, l1, dx): return (l0 + l1) * dx * 0.5

(X, Y) = primitive(f, -1, 1, -1 / 3)
plt.plot(X, Y, 'b', X, Y, 'bo')
plt.axhline()
plt.axvline()

def p(x): return (x ** 3) / 3

Y = [p(x) for x in X]
plt.plot(X, Y, 'r', X, Y, 'bo') # propagation erreur cumulative de gauche à droite
# meilleurs technique sans faire beaucoup plus de calculs

for i in range(3, 250, 10):
    (X, Y) = primitive(f, 1, 10, 0, i)
    plt.plot(X, Y)

plt.show()


def F(y, x): # fonction dépendant du point précédent calculé7
    return 1 - y # x: temps adimmensionné

def creneau(y, x): # créaneau pas d'échantillonnage un peu débile
    if x % 0.2 < 0.1: return 1 # période
    return -1

def creneau (y, x):
    if x % 2 < 1: return 1 - y
    return -1-y

dx = 1 / n
X = [0 + i * dx for i in range(n)]

# implémentation (équation différentielle)

'''t1 = 0
dt = 0.05
Y = [CI]
for i in range(n):
    Y += [Y[i] + F(Y[i], t1 + dt) * dt
    t1 += dt'''

#y' = 1 - y
#y(0) = 0

import math

def Euler(F, a, b , ci, n = 100):
    dx = (b - a) / n
    X = [a + i * dx for i in range(n + 1)]
    Y = [ci]
    for i in range(n):
        dy = F(Y[i], X[i]) * dx
        Y.append(Y[i] + dy)
    return (X, Y)

(X, Y) = Euler(F, 0, 5, 0, 100)
(X, Y) = Euler(creneau, 0, 5, 0, 100)

'''

try B

dx = 0.4
X = [i * dx for i in range(100)]

T = 0.5
Y = [2 * (-1) ** ((x // T) % 2) for x in X]

'''

plt.plot(X, Y)
plt.plot(X, [1 - math.exp(-x) for x in X])
plt.show()