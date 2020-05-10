import matplotlib.pyplot as plt

def echantillon(a, b, nb_points = 100):
    dx = (b - a) / nb_points
    return [a + i * dx for i in range(nb_points + 1)]

def parabole(x):
    return x ** 2

def d(f, x0, dx):
    return (f(x0 + dx) - f(x0)) / dx

def derivee(f, a, b, nb_points = 100):
    # infinitésimale ? Nope
    dx = (b - a) / nb_points # value recommended by teacher
    X = echantillon(a, b, nb_points)
    D = [d(f, x, dx) for x in X]
    return X, D

def derivee(X, Y):
    D = [(Y[1] - Y[0]) / (X[1] - X[0])]
    for i in range(1, len(X) - 1):
        D += [(Y[i + 1] - Y[i - 1]) / (X[i + 1] - X[i - 1])]
    D += [(Y[-1] - Y[-2]) / (X[-1] - X[-2])]
    return (X, D)

X = echantillon(1, 10)
Y = [x ** 2 for x in X]
plt.plot(X, Y)
plt.show()

a, b, l = 0, 1, 200 # plus l grand, plus d'approximation (1)
X = [a]
dx = (b - a) / l
for i in range(l):
    X += [X[-1] + dx]
    
# ou

a, b, l = 0, 1, 20
X = []
dx = (b - a) / l
for i in range(l + 1):
    X += [a + i * dx] # list comprehension sujet pour limiter approximation (peut s'alourdir cf (1))
    
print(X)

a = 2
A = 3
print(a, A)

X, D = derivee(parabole, 0, 1, 10)
plt.plot(X, D)
plt.show() # do both on same graph

plt.plot(X, D)
plt.plot(X, [parabole(x) for x in X])

V = [0, 1, 2, 3, 4, 4.4, 4.8, 5, 5.2, 5.6, 6, 7, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.5, 11.1, 11.5, 12.1, 12.55, 13.1, 14.0, 16.0, 18.0, 20]
pH = [1.3, 1.4, 1.6, 1.8, 2.1, 2.4, 2.8, 3.1, 3.5, 3.9, 4.2, 4.6, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.8, 6.1, 8.6, 11.4, 11.7, 11.8, 12.0, 12.0, 12.1, 12.2, 12.4, 12.5, 12.5]

test = [1.3, 1.4, 1.6, 1.8, 8.1, 2.4, 2.8, 3.1, 3.5, 3.9, 4.2, 4.6, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 6.5, 5.6, 5.8, 6.1, 8.6, 11.4, 11.7, 11.8, 12.0, 12.0, 12.1, 14.2, 12.4, 12.5, 12.5]

plt.plot(V, pH, 'ro')
plt.plot(X, D)

from math import sin

X, D = derivee(sin, -5, 5, 100)

def maxima(X, Y):
    Xm, Ym = [], []
    for i in range(1, len(X) - 1):
        if Y[i] > Y[i - 1] and Y[i] > Y[i + 1]:
            Xm += [X[i]]
            Ym += [Y[i]]
    return (Xm, Ym)

X, Y = maxima(V, test)
plt.plot(X, Y, 'ro')

X, D = derivee(V, pH)

for x, p, d in zip(X, pH, D):
    print(x, p, d)
    
'''

8.6 5.2 0.5
8.8 5.3 0.5 (5.4 - 5.2) / (9 - 8.6)
9 5.4 0.5000000000000022 (5.5 - 5.3) / (9.2 - 8.8) (ah ouais en fait le pc c'est juste un gros rageux...) # 9 - 8.6, 9.2 - 8.8 donc > fonctionne...
9.2 5.5 0.4999999999999978
9.4 5.6 0.7499999999999989

12.1 12.0 0.19047619047618966
12.55 12.0 0.09999999999999964 (12.1 - 12.0) / (13.1 - 12.1) = 0.1 / 1
13.1 12.1 0.1379310344827582 (12.2 - 12.0) / (14.0 - 13.55) = 0.2 / 0.45 # pas même argument pour 13.1
14.0 12.2 0.1034482758620692 (12.4 - 12.2) / (16.0 - 13.1) = 0.2 / 2.9 # maximum relatif mais pas le cas car il faut vérifier que la dérivée s'annule (voir vérifier changement de signe)
16.0 12.4 0.07500000000000018

'''

X, D = maxima(X, D)
plt.plot(X, D, 'ro')