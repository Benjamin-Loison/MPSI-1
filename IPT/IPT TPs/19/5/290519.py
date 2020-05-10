import matplotlib.pyplot as plt
import numpy as np
from numpy import random as rd, exp, sqrt, pi, sin
from scipy.integrate import odeint

z = np.zeros(5)
print(z)
print(type(z))

mz = np.zeros((5, 3))
print(mz)
print(type(mz))

a = np.ones(5)
print(a)
a.fill(7)
print(a)

print(np.eye(5)) # I5

print(np.arange(0, 2, 0.1))

print(np.linspace(0, 1, 20))

print(rd.randint(0, 10, (5, 5)))
print(rd.random(10)) # random upbound is excluded in NP but not in STL

# 1

def h(x):
    return exp(- 0.5 * x ** 2) / sqrt(2 * pi)

xt = np.linspace(-4, 4, 41)
ht = h(xt)

plt.plot(xt, ht) # courbe en cloche
plt.show()

# 2

def y(t):
    return 10 * t - 0.5 * 9.81 * t ** 2

xt = np.arange(0, 20 / 9.81, 0.1)
ht = y(xt)

plt.plot(xt, ht) # cloche plus large
plt.show()

# 3

def factoriel(n):
    if n == 0: return 1
    return factoriel(n - 1) * n

nt = range(10)
for n in nt:
    print(n, factoriel(n))

array = np.zeros(5)
print(array)
array[2] = 4

def mySin(x, n):
    terms = np.zeros(n + 1)
    fact = 1
    for j in range(n + 1):
        for k in range(max(1, j), 2 * j + 2):
            fact *= k
        terms[j] = (((-1) ** j) * (x ** (2 * j + 1)) / fact)
    return sum(terms)

def mySin(x, n):
    terms = np.zeros(n + 1)
    terms[0] = x
    fact = 1
    for j in range(n + 1):
        for k in range(max(1, j), 2 * j + 2):
            fact *= k
        terms[j] = -terms[j - 1] * (x ** (2 * j + 1)) / factoriel(2 * j + 1)
    return sum(terms)

def mySin(x, n): # use this one
    terms = np.zeros(n + 1)
    terms[0] = x
    fact = 1
    for j in range(n + 1):
        for k in range(max(1, j), 2 * j + 2):
            fact *= k
        terms[j] = -terms[j - 1] * (x ** (2 * j + 1)) / fact
    return sum(terms)

a = ((-1) ** 5) * (3 ** (2 * 5 + 1))

def mySin(x, n):
    mySum = 0
    for j in range(n + 1):
        mySum += ((-1) ** j) * (x ** (2 * j + 1)) / factoriel(2 * j + 1)
    return mySum

xt = np.linspace(0, 4 * pi, 100)
sint = [mySin(x, 20) for x in xt] # 20
plt.plot(xt, sint)
sint = sin(xt)
plt.plot(xt, sint)
plt.show()

def f(y, x):
    return y

x = np.linspace(0, 5, 100)
print(x)
y = odeint(f, 1, x)
solex = exp(x)
plt.plot(x, y, x, solex) # need zoom to see both
plt.show()

print(x * 2) # multiply all elements by '2' here

# 4

# θ'' = -sin θ
# θ' = Primitive[-sin θ]

# y' = y

def myOdeInt(X): # Euler ou autre chose
    

def pendule(X, t):
    

def euler(F, t0, tf, y0, n):
    """Données:
    F(y,t) une fonction
    t0,t1 deux réels avec t0 < t1
    y0 un réel
    n un entier
    Résultat: le tuple constitué de la liste des temps [t0,...,tn] et la liste des (n+1) réels [y_0, ...y_n]
    qui constituent une approximation de la solution y sur [t0,tf]
    de l’ED y’=F(y,t) avec la condition initiale y(t0) = y0
    """
    h = (tf-t0)/n
    y = y0
    t = t0
    Y = [y0]
    T = [t0]
    for k in range(n):
        y = y + h*F(y,t)
        t = t + h
        Y.append(y)
        T.append(t)
    return T,Y

def F(Y,t):
    """Données: t un flottant, Y un tableau de deux flottants"
    Résulat: un tableau de deux flottants
    """
    theta,thetap = Y
    7
    return np.array([thetap, - np.sin(theta)])

temps = np.linspace(0, 6*np.pi, 100)
sol = odeint(F, [0, 0.5], temps)
theta , thetap = sol[:, 0], sol[ :, 1]
plt.plot(temps, theta)
plt.show()


y0 = np.array([0, 0.5])
sol = euler(F,0, 6*np.pi,y0,1000)

temps, Y = sol[0], sol[1] # attention Y est une liste de array
Y = np.array(Y)
theta, thetap = Y[:, 0], Y[ :, 1]
plt.plot(temps, theta)
plt.show()

def f(Y, l=0.30, g=9.80665):
    r""" L'opérateur :math:`f: Y \mapsto f(Y)` :eq:`operateur_f`, écrit comme une fonction Python.

    .. math::
       :label: operateur_f

       \frac{dY}{dt} &= \Big[\frac{d\theta}{dt}, \frac{d^2\theta}{dt^2}\Big] \\
                     &= [\dot\theta, - (g/l) \sin(\theta)] \\
                f(Y) &= [Y_1, - (g/l) \sin(Y_0)]


    - *Arguments :*
       - ``Y`` est tableau ``numpy`` monodimensionnel (à deux éléments) et renvoie un tableau numpy de même taille. :math:`Y = [\theta, \dot\theta]` donc :math:`Y_0 = \theta, Y_1 = \dot\theta`,
       - (optionnel) ``g`` est l'accélération de la pesanteur à la surface de la Terre (:math:`g = 9.80665 \; m/s^2`),
       - (optionnel) ``l`` est la longueur de la tige (:math:`l = 30` cm dans les applications).

    - Exemple :

    >>> Y = np.array([0, 10]); print(Y)
    [ 0 10]
    >>> l = 0.30; g = 9.80665
    >>> print(f(Y, l, g))
    [10  0]
    >>> Y = np.array([10, 5])
    >>> print(f(Y, l, g))
    [ 5 17]
    >>> l = 0.60  # Une corde plus longue => plus faible vitesse
    >>> print(f(Y, l, g))
    [5 8]
    """
    fY = np.zeros_like(Y)
    fY[0] = Y[1]
    fY[1] = - (g / l) * np.sin(Y[0])
    return fY

def euler(h, tmax, theta0, thetaPoint0):
    r"""
    Résoud numériquement l'équation différentielle d'ordre 2 du pendule simple :eq:`pendule` par `la méthode d'Euler <https://fr.wikipedia.org/wiki/M%C3%A9thode_d%27Euler>`_ pour :math:`t \in [0, t_{\max}]`, avec un pas de temps :math:`h > 0`.

    .. math:: \frac{d^2 \theta}{d t^2}(t) + \frac{g}{l} \sin(\theta(t)) = 0.
       :label: pendule


    Pour utiliser un schéma d'Euler, il nous faut écrire cette équation (ordinaire d'ordre 2, mais *non linéaire !*) sous la forme :math:`Y'(t) = f(t, Y)`, où :math:`Y = [\theta, \dot\theta]` :

    .. math:: f(Y) = [Y_1, - (g/l) \sin(Y_0)]

    Et dès lors, le schéma de mise à jour d'Euler s'écrit :

    .. math:: Y_{i+1} = Y_i + (t_{i+1} - t_i) \times f(t_i, Y_i)

    Mais dans notre cas, les temps discrets :math:`t_i` sont *uniformément* espacés,
    donc :math:`\forall i \in \{0,\dots,n-1\},\; t_{i+1} - t_{i} = h` (le *pas de temps*), donc le schéma se simplifie en :eq:`schemaeuler` :

    .. math:: Y_{i+1} = Y_i + h \times f(t_i, Y_i)
       :label: schemaeuler


    - L'opérateur :math:`f: (t, Y) \mapsto f(t, Y)` est vectoriel (de taille :math:`2 \times 2`), et il est donné par la fonction :func:`f`.
    - Les conditions initiales sont données par ``theta0`` et ``thetaPoint0``.

    - Renvoit un tableau (``list``) contenant les valeurs de :math:`u_c` calculées aux instants :math:`t_i = i \times h` (pour :math:`0 \leq i \leq t_{\max} / h)`.

    - *Arguments* :
       - ``h`` est un pas de temps (:math:`h > 0`),
       - ``tmax`` est la durée totale de la simulation numérique (:math:`t_{\max} > 0`),
       - ``theta0``:math:`= \theta_0` est la valeur de :math:`\theta(t=0)`,
       - et ``thetaPoint0``:math:`= \dot{\theta_0}` est la valeur de :math:`\dot\theta(t=0) = \left(\frac{d\theta}{dt}\right)(t=0)`.

    - *Hypothèse* : On résoudra l'équation pour :math:`t \geq 0`.

    - Exemple (question I.2.c) :

    >>> theta0 = 0
    >>> thetaPoint0 = 6
    >>> tmax = 5
    >>> nbPoints = 2000  # On choisit 2000 points
    >>> h = tmax / nbPoints
    >>> thetas = euler(h, tmax, theta0, thetaPoint0)
    >>> np.shape(thetas)
    (2000, 2)
    >>> thetas[0]  # Vérifions les conditions initiales
    array([ 0.,  6.])
    >>> thetas[-1]  # Dernière valeur ?  # doctest: +ELLIPSIS
    array([ 0.988...,  4.510...])
    >>> maxTheta = max(thetas[:, 0])  # Plus grand angle atteint
    >>> maxTheta  # doctest: +ELLIPSIS
    1.277...
    >>> maxThetaPoint = max(thetas[:, 1])  # Plus grande vitesse atteinte
    >>> maxThetaPoint  # doctest: +ELLIPSIS
    7.013...

    - Courbe :math:`(t, \theta(t))`, on constate déjà que ce n'est pas exactement une solution harmonique (il y a une légère amplification due aux erreurs numériques introduites par l'approximation de Taylor qui justifie le schéma de mise à jour de la méthode d'Euler) :

    .. image:: TP5__euler_ordre2_position.png
       :align: center
       :scale: 80%

    - Portrait de phase (:math:`(\theta(t), \dot\theta(t))`), qui n'est pas un cercle et donc on constate que la méthode d'Euler n'est pas exacte pour cette simulation :

    .. image:: TP5__euler_ordre2_vitesse.png
       :align: center
       :scale: 80%

    - Complexité en *temps* : :math:`O(n)`, avec :math:`n = \lceil t_{\max} / h \rceil`.

    - Complexité en *mémoire* (question I.2.c) : des constantes, plus un tableau numpy de flottants sur 64 bits (``numpy.float64``, soit 4 octets), de taille exactement :math:`(n, 2)`, avec :math:`n = \lceil t_{\max} / h \rceil` (la taille d'un tableau numpy peut être obtenue avec la fonction :func:`numpy.shape`).
    - Exemple :

    >>> h = 0.001; tmax = 60
    >>> n = int(np.ceil(tmax / h))
    >>> memoire = 4 * 2 * n  # Pour le numpy array de taille (n, 2)
    >>> print("La procedure euler consommera de l'ordre de %g octets..." % memoire)
    La procedure euler consommera de l'ordre de 480000 octets...
    >>> print("Soit environ %g Ko (ca reste tres raisonnable !)." % (memoire / 1024))
    Soit environ 468.75 Ko (ca reste tres raisonnable !).
    """
    i_max = int(np.ceil(tmax / h))
    # On créé un tableau qu'on va remplir petit à petit
    thetas = np.zeros((i_max, 2))
    # Conditions initiales
    thetas[0, 0] = theta0
    thetas[0, 1] = thetaPoint0
    # Iteration
    for i in range(0, i_max - 1):
        # On applique la relation d'Euler vectorielle
        thetas[i + 1] = thetas[i] + h * f(thetas[i])
    return thetas

def portraitPhase(thetas, methode="par méthode d'Euler"):
    r""" Trace le portrait de phase, soit la dérivée :math:`\dot\theta` en fonction de la valeur de l'angle :math:`\theta`.

    - *Argument*:
       - ``theta`` est un *array-like* (liste ou numpy array) de taille :math:`(n, 2)`, qui contient les valeurs (approchées ou non) de :math:`Y = [\theta, \dot\theta]` aux instants :math:`t_i`.

    .. image:: TP5__euler_ordre2_vitesse.png
       :align: center
       :scale: 120%
    """
    plt.figure()
    X = thetas[:, 0]
    Y = thetas[:, 1]
    plt.plot(X, Y, 'b-')
    plt.grid()
    plt.xlabel(r"Angle $\theta$ (en radian)")
    plt.ylabel(r"Vitesse angulaire $\dot\theta$ (en radian par seconde)")
    plt.title("Portrait de phase du pendule pesant simple {}.".format(methode))
    plt.show()

def tracerCourbe(listeTemps, theta, methode="par méthode d'Euler"):
    r""" Trace la courbe :math:`\theta(t)`, valeur de l'angle :math:`\theta` en fonction du temps :math:`t`.

    - *Arguments*:
       - ``listeTemps`` est un *array-like* (liste ou numpy array) contenant les valeurs :math:`t_i`,
       - ``theta`` contient les valeurs (approchées ou non) de :math:`\theta_i = \theta(t_i)`.

    .. image:: TP5__euler_ordre2_position.png
       :align: center
       :scale: 120%
    """
    X = listeTemps
    Y = theta
    plt.figure()
    plt.plot(X, Y, 'r-')
    plt.grid()
    plt.xlabel(r"Valeur discrète du temps $t$")
    plt.ylabel(r"Angle $\theta$ (en radian)")
    plt.title("Résolution du pendule pesant simple {}.".format(methode))
    plt.show()

# %% Exercice I.2
# if __name__ == '__main__':
print("Resolution approche du pendule pesant simple par methode d'Euler, exemple I.2.c")
methode = "par méthode d'Euler"
theta0 = 0
thetaPoint0 = 6
tmax = 5
nbPoints = 2000
h = tmax / nbPoints
# On calcule la solution
thetas = euler(h, tmax, theta0, thetaPoint0)
# Affichages
listeTemps = np.linspace(0, tmax, nbPoints)
print("Affichage de la courbe theta(t)...")
tracerCourbe(listeTemps, thetas[:, 0], methode=methode)
print("Affichage du portrait de phase (theta, thetaPoint)... \n ==> Ce n'est pas un vrai cercle !")
portraitPhase(thetas, methode=methode)

def pend(y, t):
    theta, omega = y
    dydt = [omega, - np.sin(theta)]
    return dydt
    
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 50, 101)
sol = odeint(pend, y0, t)

plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

# cf cours

# { v = A'
# { v' = -w²sin A (A: angle)
# { A0, v0
# reconstruire theta puis theta'