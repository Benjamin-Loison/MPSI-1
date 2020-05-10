# -*- coding: utf-8 -*-
"""                             TP 5
                    Conversions décimal -> binaire
         @author: Sébastien RÉAU - sebastien.reau@fenelon.lyc.fr


Le travail demandé est indiqué au fur et à mesure ci-dessous.
Les questions doivent être traitées dans l'ordre de cet énoncé.
"""


# I. 1. Création de la liste des puissances de 2

nombre = 1789 # nombre à décomposer 
puissance = 1
puissances = [] 
while puissance <= nombre :
    puissances = puissances + [puissance]
    puissance = puissance * 2
puissances # pour visualiser le contenu de la liste "puissances"


## I Algorithme "table des puissances de 2"

# 1 Création de la table des puissances 2 ** k

# a

nombre = 42
k = 0
puissances = []

while 2 ** k <= nombre:
    puissances += [2 ** k]
    k += 1
    
print(puissances)

# b lesson

nombre = 42
puissance = 1
puissances = []

while puissance <= nombre:
    puissances += [puissance]
    puissance *= 2

print(puissances)

# b alpha (personal)

nombre = 42
puissances = [1]

while puissances[len(puissances) - 1] * 2 <= nombre:
    puissances += [puissances[len(puissances) - 1] * 2]

print(puissances)

# b beta (personal)

nombre = 42
puissances = [1] # could be done: find with math proccess the biggest power of 2 of 42 and decrement and construct the table from the greatest to the lowest

while puissances[len(puissances) - 1] * 2 <= nombre:
    puissances += [puissances[len(puissances) - 1] * 2]

print(puissances)

# b charlie (2 lesson reversed)

nombre = 42
puissance = 1
puissances = []

while puissance <= nombre:
    puissances = [puissance] + puissances
    puissance *= 2

print(puissances)

# I. 2 Soustractions successives

codage = ''
N = nombre # pour laisser intact le nombre entré plus haut

"""
Remplacez ce commentaire par la suite des lignes de code
traduisant en Python l'algorithme proposé dans l'énoncé papier.
L'affichage du résultat est assuré par les 2 instructions ci-dessous.
"""

# 2 Soustraction successives

# b charlie version for the beginning

nombre = 42
initNumber = nombre
puissance = 1
puissances = []

while puissance <= nombre:
    puissances = [puissance] + puissances
    puissance *= 2

# end b charlie version

codage = "" # contains list of binary digit representing the number in base 2

for puissance in puissances: # warning: puissances here need to be treated from the greatest to the lowest
    testValue = nombre - puissance
    if testValue >= 0:
        codage += '1'
        nombre = testValue
    else:
        codage += '0'

# patch for displaying 0 for the special case
#if codage == "":
#    print(0)
#else:
#    print(codage)

print("Représentation de " + str(initNumber) + " en base 2 : " + codage)
print("A comparer avec le résultat de la fonction \"bin\" : " + bin(initNumber)) # 0b + binary

# reverse loop
# b lesson

nombre = 42
puissance = 1
puissances = []

while puissance <= nombre:
    puissances += [puissance]
    puissance *= 2

print(puissances)

codage = "" # contains list of binary digit representing the number in base 2

for puissance in range(len(puissances) - 1, -1, -1): # warning: puissances here need to be treated from the greatest to the lowest
    testValue = nombre - puissances[puissance]
    if testValue >= 0:
        codage += '1'
        nombre = testValue
    else:
        codage += '0'
        
# patch for displaying 0 for the special case
if codage == "":
    print(0)
else:
    print(codage)

# II. Divisions entières

"""
Remplacez ce commentaire par vos lignes de code.
Pour l'affichage du résultat, il est conseillé de faire un
copier-coller des instructions précédentes.
"""

## II Algorithme "divisions entières par 2"

binaryNumber = ""
number = 42

while number >= 1:
    binaryNumber = str(number % 2) + binaryNumber
    number //= 2

# patch for displaying 0 for the special case
if binaryNumber == "":
    print(0)
else:
    print(binaryNumber)

# III. Améliorations éventuelles

"""
Modifiez l'algorithme du I si vous voyez des simplifications
à y apporter.

Si ces 2 algorithmes ne fonctionnent pas pour nombre = 0,
ajouter les lignes nécessaires prenant en compte ce cas particulier.
"""

# IV. Passage à la base 16

"""
Copiez-collez ici l'algorithme des divisions entières successives.
Modifiez-le de sorte qu'il donne la représentation hexadécimale
du nombre choisi.

Rappel : en base 16, la représentation d'un nombre nécessite
16 caractères. Ces 16 caractères sont 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
puis A, B, C, D, E et F ; le A codant 10, B : 11, C : 12, D : 13, 
E : 14 et F : 15.

Exemple : 1789 s'écrit en base 16 : 6FD 
               car 1789 = 6*(16**2) + 15*(16**1) + 13*(16**0)
"""

## II Algorithme "divisions entières par baseLen"

finalNumber = ""
number = 1789
base = "0123456789ABCDEF"
baseLen = len(base)

while number >= 1:
    finalNumber = base[number % baseLen] + finalNumber
    number //= baseLen

# patch for displaying 0 for the special case
if finalNumber == "":
    print(0)
else:
    print(finalNumber)

# if statement

#from random import randint as rand 

#rand(1,5)

testNumber = 16
testCondition = 0
baseLen = 16
for number in range(1, testNumber + 1):
    finalNumber = ""
    condition = 0
    
    while number >= 1: # 0 needed for stats
        reminder = number % baseLen
        print(reminder)
        toAdd = ''
        if reminder < 10:
            toAdd = str(reminder)
            condition += 1
        elif reminder == 10:
            toAdd = 'A'
            condition += 2
        elif reminder == 11:
            toAdd = 'B'
            condition += 3
        elif reminder == 12:
            toAdd = 'C'
            condition += 4
        elif reminder == 13:
            toAdd = 'D'
            condition += 5
        elif reminder == 14:
            toAdd = 'E'
            condition += 6
        else:
            toAdd = 'F'
            condition += 6
        finalNumber = toAdd + finalNumber
        number //= baseLen
    
    testCondition += condition
print(testCondition, testNumber, testCondition / testNumber)
    #print(condition)
    
    # patch for displaying 0 for the special case
    #if finalNumber == "":
    #    print(0)
    #else:
    #    print(finalNumber)

testNumber = 16
testCondition = 0
baseLen = 16
for number in range(testNumber):
    finalNumber = ""
    condition = 0
    
    while number >= 1:
        reminder = number % baseLen
        toAdd = ''
        if reminder == 10:
            toAdd = 'A'
            condition += 1
        elif reminder == 11:
            toAdd = 'B'
            condition += 2
        elif reminder == 12:
            toAdd = 'C'
            condition += 3
        elif reminder == 13:
            toAdd = 'D'
            condition += 4
        elif reminder == 14:
            toAdd = 'E'
            condition += 5
        elif reminder == 15:
            toAdd = 'F'
            condition += 6
        else:
            toAdd = str(reminder)
            condition += 6
        finalNumber = toAdd + finalNumber
        number //= baseLen
    
    testCondition += condition
print(testCondition, testNumber, testCondition / testNumber)