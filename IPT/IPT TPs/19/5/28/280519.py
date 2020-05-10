import matplotlib.pyplot as plt

def v(t):
    if t >= 0 and t <= 1: return 5 * t ** 2
    elif t >= 1 and t <= 4: return 10 * t - 5
    elif t >= 4 and t <= 5: return -5 * t ** 2 + 50 * t - 85
    return 0

nb_points = 100
#dt = 5 / N
#T = [k * dt for k in range(N + 1)]
#V = [v(t) for t in abs]

def echantillon(f, a, b, nb_points = 100):
    dt = (b - a) / nb_points
    X = [a + dt * k for k in range(nb_points)]
    Y = [f(t) for t in X]
    return (X, Y)

(T, V) = echantillon(v, 0, 5)
plt.plot(T, V)
plt.show()

def rectangle(x, y):
    return x * y

N = 100
(T, trash) = echantillon(v, 0, 5, N)
dt = 5 / N
print(sum([rectangle(dt, v(t)) for t in T]))

# 50
# 90
# 99.00000000000001

def v(t):
    return -1

# -5
# -5
# -4.99999999999

# extensiosn à des bornes quelconques a et b (comprises entre 0 et 5, ou non) ?

def trapeze(x, y, yNext):
    return x * (yNext + y) / 2

N = 101
(T, trash) = echantillon(v, 0, 5, N)
dt = 5 / N
print(sum([trapeze(dt, v(T[i]), v(T[i + 1])) for i in range(len(T) - 1)]))

# 43.0555556
# 82.05296769346354
# 98.0201052896193

V = [sum([trapeze(dt, v(T[i]), v(T[i + 1])) for i in range(r - 1)]) for r in range(len(T))]

T += [5]
V += [V[-1] + v(5) * dt]

def f(x): return 4 / (1 + x ** 2)

def p(x): return 8 * x / ((1 + x ** 2) ** 2)
(T, V) = echantillon(p, 0, 1, N)
# right way to do it ?

V = (0.00, 0.11, 0.42, 0.86, 1.47, 2.21, 3.05, 3.92, 4.77, 5.63, 6.42, 7.03, 7.45, 7.64, 7.63, 7.45, 7.07, 6.59, 6.02, 5.42, 4.86, 4.36, 3.89, 3.45, 3.13, 2.93, 2.86, 2.89, 3.03, 3.25, 3.54, 3.86, 4.19, 4.51, 4.81, 5.09, 5.35, 5.56, 5.72, 5.81, 5.84, 5.81, 5.75, 5.66, 5.54, 5.40, 5.26, 5.11, 4.96, 4.83, 4.71, 4.59, 4.47, 4.37, 4.29, 4.23, 4.20, 4.18, 4.19, 4.20, 4.22, 4.25, 4.28, 4.31, 4.33, 4.35, 4.37, 4.38, 4.39, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40, 4.40)

def d(t): # need to manage give t = 0.XY5 ? and more than 1 ?
    distance = 0
    if t > 1:
        distance += 4.4 * (t - t % 1)
        t %= 1
    for i in range(int(t // 0.01)):
        distance += 0.01 * V[i]
    return distance

(T, V) = echantillon(d, 0, 5)
plt.plot(T, V)
plt.show()