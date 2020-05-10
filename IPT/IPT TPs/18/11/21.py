# -*- coding: utf-8 -*-
"""                      TP 4 (à compléter)
                            Boucle WHILE
         @author: 
"""



# Mot de passe : code du TP 2 à modifier
#------------------------------------------------------------------------------

isFine = False;
while not isFine:
    pwd = input('Choisissez un mot de passe SVP : ')
    if len(pwd) < 6 :
        print('Trop court !')
    elif len(pwd) > 8 :
        print('Trop long !')
    else :
        pwd2 = input('Confirmez : ')
        if pwd2 == pwd :
            print('OK')
            isFine = True
        else :
            print('Erreur')
print(pwd)

# Recherche d'une sous-chaîne : code du TP 3 à modifier
#------------------------------------------------------------------------------

texte = "Ah, qu'est-ce qu'on est serré au fond de cette boîte !"
mot = "!"
L_texte = len(texte)
L_mot = len(mot) # pour ne pas recalculer plusieurs fois ces deux nombres
found = False
k = 0
while k < L_texte - L_mot + 1 and not found:
    if texte[k : k+L_mot] == mot :
        found = True
    k += 1
if not found :
    print("Non trouvé")
else :
    # le compteur reste affecté du bon indice en sortie de boucle
    print("Trouvé en position : " + str(k))


# Division entière
#------------------------------------------------------------------------------

dividende = 16540
dividendeTmp = dividende
diviseur = 177
quotient = 0

while dividendeTmp >= diviseur:
    dividendeTmp -= diviseur
    quotient += 1
reste = dividendeTmp

# Affichage du résultat
print(str(dividende) + ' // ' + str(diviseur) + ' = ' + str(quotient)
      + ' (reste ' + str(reste) + ')')
 
# Le juste prix
#------------------------------------------------------------------------------

from random import randint as randInt # à exécuter une fois pour toutes
N = randInt(1, 1000)
message = "J'ai choisi un entier compris entre 1 et 1000. Devine-le : "
user = 0
while user != N:
    user = int(input(message))
    if user < N:
        print("Greater")
    elif user > N:
        print("Lower")

from random import randint as randInt # à exécuter une fois pour toutes
N = randInt(1, 1000)
N = 512
counter = 1
lowerBound = -1
user = 0
while user != N:
    if counter == 1:
        user = int(input("J'ai choisi un entier compris entre 1 et 1000. Devine-le : "))
        lowerBound = user
        justDefined = True
    counter += 1
    if user > N:
        user = int(input("Plus petit... Essaie encore : "))
    elif user < N:
        if user > lowerBound or justDefined:
            lowerBound = user
            user = int(input("Plus grand... Essaie encore : "))
            justDefined = False
        else:
            user = int(input("Oh ! J'avais dit plus grand que " + str(lowerBound) + " !!! Essaie encore : "))
print("Gagné en " + str(counter) + " coup(s) !")

#

lowerBound = 1
upperBound = 1000
user = int(input("Nombre entre " + str(lowerBound) + " et " + str(upperBound) + ": "))
computer = 500
lastComputer = computer
counter = 1
answer = input("Est-ce que c'est " + str(computer) + " ? (o/+/-) : ")
if answer == '-':
    lastComputer = lowerBound
elif answer == '+':
    lastComputer = upperBound
while answer != 'o':
    counter += 1
    if answer == '-':
        computerTmp = (lastComputer + computer) // 2
        answer = input("Plus petit que " + str(computer) + "... Est-ce que c'est " + str(computerTmp) + " ? (o/+/-) : ")
        lastComputer = computer
        computer = computerTmp
    elif answer == '+':
        computerTmp = (lastComputer + computer) // 2
        answer = input("Plus grand que " + str(computer) + "... Est-ce que c'est " + str(computerTmp) + " ? (o/+/-) : ")
        lastComputer = computer
        computer = computerTmp
print("J'ai trouvé en " + str(counter) + " coup(s) ! Bogoss ^^")