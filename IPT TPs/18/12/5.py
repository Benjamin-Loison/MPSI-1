# -*- coding: utf-8 -*-
"""                             TP 6
                      Procédures et fonctions
         @author: 
"""


#------------------------------------------------------------------------------
""" Carré + diagonale """
#------------------------------------------------------------------------------

# Rappel du code
#---------------
N = 12
print(N*'* ')
for i in range(N-2) :
    print('* ' + i*'  ' + '* ' + (N-i-3)*'  ' + '* ')
print(N*'* ')


# Définition de la procédure carre
#---------------------------------

def carre(taille, motif):
    print(taille * (motif + ' '))
    for i in range(taille - 2) :
        print((motif + ' ') + i * '  ' + motif + ' ' + (taille - i - 3) * '  ' + motif + ' ')
    print(taille * (motif + ' '))
    # lignes de codes à placer dans ce bloc indenté
    # pas de return dans une procédure


# Utilisation depuis la console
#------------------------------
# Tester la bonne exécution des commandes suivantes :
# >>> carre(10, '*')
# >>> carre(17, 'o')


#------------------------------------------------------------------------------
""" L'affaire de quelques secondes """
#------------------------------------------------------------------------------

def conversion(N):
    j = N // 86400
    h = (N % 86400) // 3600
    min = (N % 3600) // 60
    s = N % 60
    return (j, h, min, s) # pour renvoyer plusieurs valeurs, on renvoie 1 seul
                          # objet, de type tuple, contenant ces valeurs
                          
def conversion(N):
    # nombre de jours en premier
    j = N // 86400
    N -= j * 86400
    h = j // 3600
    N -= h * 3600
    min = N // 60
    N -= min * 60
    s = N % 60
    return (j, h, min, s)
    
def conversion(N):
    # nombre de secondes en premier
    s = N % 60
    N -= s
    min = (N % 3600) // 60
    N -= min * 60
    h = (N % 86400) // 3600
    N -= h * 3600
    j = N // 86400
    return (j, h, min, s)
    
def conversion(N):
    # nombre de secondes en premier
    s = N % 60
    N -= s
    min = (N % 3600) // 60
    N -= min * 60
    h = (N % 86400) // 3600
    N -= h * 3600
    j = N // 86400
    return ((j, "jour"), (h, "heure"), (min, "minute"), (s, "seconde"))
                          
def dateType(number, name):
    dateTypeStr = ""
    if number != 0:
        if number == 1:
            dateTypeStr += "1 " + name + " "
        else:
            dateTypeStr += str(number) + " " + name + "s "
    return dateTypeStr

def convertir(N) :
    dateStr = ""
    dateTuple = conversion(N)
    for i in range(len(dateTuple)):
        dateTupleIndex = dateTuple[i]
        dateStr += dateType(dateTupleIndex[0], dateTupleIndex[1])
    return dateStr

#------------------------------------------------------------------------------
""" 365,25 """
#------------------------------------------------------------------------------

def is_bissextile(an):
    if (an % 4) == 0:
        if (an % 100) == 0:
            return (an % 400) == 0
        else:
            return True
    return False

def is_bissextile(an):
    return (an % 4) == 0 and (((an % 100) == 0 and (an % 400) == 0) or (an % 100) != 0)
   # /!\ programme extérieur appelant la fonction is_bissextile
# /!\ à exécuter dans une console IPython pour bien interpréter le input

annee = int(input("Donnez-moi une année SVP : "))
if is_bissextile(annee) :
    print(str(annee) + " est bissextile.")
else :
    print(str(annee) + " n'est pas bissextile.")


#------------------------------------------------------------------------------
""" Variations autour de sqrt """
#------------------------------------------------------------------------------

def is_carre(number): # found True for the subject number in several seconds
    i = 0
    powered = 0
    while powered < number:
        i += 1
        powered = i ** 2
    return powered == number
    
import time
    
def is_carre(number):
    # dichotomie
    i = number // 2
    powered = i ** 2
    while powered != number:
        if powered < number:
            i //= 2
        else:
            i += (number - i) // 2
        print(i)
           # time.sleep(1)
        powered = i ** 2
    return powered == number
    
def mySqrt(positiveReal):
    i = int(positiveReal)
    while i * i > positiveReal:
        i -= 1
    return i
    
for val in reversed(range(0, 20, 2)): # lowerBound (int), upperBound (int), step (int)
    print(val)

def renverser(list):
    reversedList = []
    for element in list:
        reversedList = [element] + reversedList
    return reversedList

def renverser(list):
    reversedList = ()
    for element in list:
        reversedList = (element,) + reversedList
    return reversedList

L = ("C'est", "la", "danse", "des", "canards.")
# L.reverse()
L = renverser(L)
# L = list(enumerate(L))
for val in L:
    print(val)

L = [1, 2, 4, 8, 16, 32, 64, 128]
for (i, val) in enumerate(L):
    print(i, val)

type(enumerate(L))

#

tu = (1, 2)
tu += (3,)

#

def egrenage(list):
    newList = ()
    for i in range(len(list)):
        newList += ((i, list[i]),)
    return newList

L = ("C'est", "la", "danse", "des", "canards.")
L = egrenage(L)
for val in L:
    print(val)

#

chiffres = (1, 1, 0, 1, 1, 0)
puissances = (32, 16, 8, 4, 2)
for (chiffre, puissance) in zip(chiffres, puissances):
    print(str(chiffre) + ' x ' + str(puissance))

type(zip(chiffres, puissances))

def min(a, b):
    if a < b:
        return a
    return b

def myZip(list0, list1):
    zipList = ()
    for i in range(min(len(list0), len(list1))):
        zipList += ((list0[i], list1[i]),)
    return zipList

L = zip(chiffres, puissances)
for val in L:
    print(val)
    
L = myZip(chiffres, puissances)
for val in L:
    print(val)

def valeur(numberList, base):
    number = 0
    length = len(numberList)
    for i in reversed(range(length)):
        number += numberList[i] * base ** (length - (i + 1))
    return number

print(valeur((1, 1, 0, 1, 1, 0), 2))
print(valeur((1, 1, 0, 1, 1, 0), 10))