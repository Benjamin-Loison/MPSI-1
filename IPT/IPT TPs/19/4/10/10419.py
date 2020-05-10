# -*- coding: utf-8 -*-
"""
                       TP 11 : Pivot de Gauss
          @author: Sébastien RÉAU - sebastien.reau@ac-paris.fr        
"""

import math

# I. Définition de variables globales

# 1 - système à résoudre : matrices A et B

A  = [[-1, -6, 1, 1, 1, 1, 1]] ; B  = [[12]]
A += [[2, -1, 1, 1, 1, 1, 1]] ; B += [[25]]
A += [[1, 1, -1, 1, 1, 1, 1]] ; B += [[22]]
A += [[1, 4, 1, -1, 1, 1, 1]] ; B += [[26]]
A += [[1, 1, 1, 1, -1, 1, 1]] ; B += [[18]]
A += [[1, 1, 1, 1, 1, -1, 1]] ; B += [[16]]
A += [[1, 1, 1, 1, 1, 1, -1]] ; B += [[14]]

# 2 - taille du système à résoudre : entier N

N = len(A)

# 3 - fabrication de la matrice A bordée de B : matrice M

def systeme() :
    return [A[i] + B[i] for i in range(N)]

M = systeme()
    
# 4 - pour voir au fur et à mesure le système se triangulariser :
#     procédure d'affichage d'une liste de listes sous la forme d'une matrice

def afficher(matrice) :
    for i in range(N): print(matrice[i])

afficher(M)

# II. Méthode du pivot partiel

# 1 - fonction détectant la ligne contenant le pivot partiel de la colonne k
#     à partir de l'élément diagonal M[k][k](inclus)

def detection_pivot(k):
    max = math.fabs(M[k][k])
    line = k
    for i in range(k + 1, N):
        if math.fabs(M[i][k]) > math.fabs(max):
            max = M[i][k]
            line = i
    return line

print(detection_pivot(0))
print(detection_pivot(1))
print(detection_pivot(2)) # 1 3 2

# 2 - procédure d'échange de 2 lignes de la matrice M

def echanger(i1, i2):
    """global M
    new = M[:]
    new[i1] = M[i2]
    new[i2] = M[i1]
    M = new"""
    
    tmp = M[i1]
    M[i1] = M[i2]
    M[i2] = tmp
    
    """for i in range(min(i1, i2)):
        new += [M[i]]
        
    if i1 < i2:
        new += [M[i2]]
    else:
        new += [M[i1]]
        
    for i in range(max(i1, i2)):
        new += [M[i]]
    
    if i1 < i2:"""

echanger(0, 1)
afficher(M)

def addLines(L1, coef):
    return [L1[k] + coef for k in range(N + 1)]
    
def addLines(L1, L2):
    return [L1[k] + L2[k] for k in range(N + 1)]

def multiplyLines(L1, coef):
    return [coef * L1[i] for i in range(N + 1)]

# 3 - procédure d'obtention des 0 sous le coefficient diagonal de la colonne k
#     (qui est censé être le pivot partiel), par remplacement de la ligne i > k
#     par CL des équations i et k suivante : Li <- Li - coef_i/pivot_k.Lk
def transvections(k):
    for i in range(k + 1, N):
        M[i] = addLines(M[i], multiplyLines(M[k], -M[i][k] / M[k][k]))

M = systeme()
afficher(M)
transvections(0)
afficher(M)
print(detection_pivot(1))
echanger(3, 1)
afficher(M)
transvections(1)
afficher(M)

# 4 - obtention du système triangulaire équivalent

""" Redéfinir la matrice système, obtenir et visualiser le système "équivalent"
    (aux approximations de calculs en représentation flottante près)."""

M = systeme()

for k in range(N - 1) :
    afficher(M) ; print()
    echanger(detection_pivot(k), k)
    transvections(k)

afficher(M)

# III. Remontée des résultats (contrainte : ne pas utiliser la fonction sum)

""" Calculer et visualiser à la console la solution du système en executant 
    la fonction resoudre() """

def resoudre():
    X = [0] * N
    X[N - 1] = M[N - 1][N] / M[N - 1][N - 1]
    for line in range(N - 2, -1, -1):
        sum = 0
        for column in range(N - 1, line, -1):
            sum += M[line][column] * X[column]
        X[line] = (M[line][N] - sum) / M[line][line]
    return X

X = resoudre()
print(X)

# check

for line in range(N):
    sum = 0
    #print(line, N)
    for column in range(line, N):
        #print(line, column, M[line][column])
        sum += M[line][column] * X[column]
    print(sum, M[line][N])

# IV. Compléments
    
# 1 - amélioration de l'affichage d'une matrice de flottants

def afficher2(matrice) :
    for L in matrice :
        ligne = ''
        for case in L :
            ligne += '{:>10.2e}'.format(case)
        print('[' + ligne + '  ]')

afficher2(M)

# 2 - de l'apparition de faux zéros dans la partie triangulaire inférieure
    
A  = [[-1, 2, 1, 1, 1, 1, 1]] ; B  = [[28]]
A += [[1, -1, 1, 1, 1, 1, 1]] ; B += [[24]]
A += [[1, 1, -1, 1, 1, 1, 1]] ; B += [[22]]
A += [[1, 1, 1, -1, 1, 1, 1]] ; B += [[20]]
A += [[1, 1, 1, 1, -1, 1, 1]] ; B += [[18]]
A += [[1, 1, 1, 1, 1, -1, 1]] ; B += [[16]]
A += [[1, 1, 1, 1, 1, 1, -1]] ; B += [[14]]

""" Tester l'algorithme sur ce système, 
    remarquer les faux zéros dans le système triangulaire obtenu. """

M = systeme()

for k in range(N-1) :
    echanger(detection_pivot(k), k)
    transvections(k)

afficher2(M)
resoudre() # fonctionne non ?

# 3 - cas particulier d'une matrice d'entiers : redéfinir la
#     procédure d'obtention des 0 sous le coefficient diagonal de la colonne k

#     avec la contrainte de ne pas fabriquer de flottants, par la formule :
#     Li <- pivot_k.Li - coef_i.Lk

#     par CL des équations i et k suivante : Li <- Li - coef_i/pivot_k.Lk

def transvections2(k):
    for i in range(k + 1, N):
        #M[i] = addLines(M[i], multiplyLines(M[k], -M[i][k] / M[k][k]))
        M[i] = addLines(multiplyLines(M[i], M[k][k]), multiplyLines(M[k], -M[i][k]))
            
# 4 - amélioration de l'affichage d'une matrice d'entiers

def afficher3(M) :
    for L in M :
        ligne = ''
        for case in L :
            ligne += '{:>10d}'.format(case)
        print('[' + ligne + '  ]')
  
afficher3(M)
  
# 5 - résolution du système

""" Redéfinir la matrice système, obtenir le nouveau système, cette fois-ci parfaitement    équivalent au système initial et en visualiser à la console la solution. """

M = systeme()

for k in range(N - 1) :
    afficher3(M) ; print ()
    echanger(detection_pivot(k), k)
    transvections2(k)

afficher3(M)
resoudre() # it works !