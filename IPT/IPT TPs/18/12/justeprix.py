# -*- coding: utf-8 -*-
"""                             TP 4
                            Boucle WHILE
         @author: Sébastien RÉAU - sebastien.reau@fenelon.lyc.fr
"""


# Le juste prix (à exécuter en console IPython)

from random import randint as tirage # à exécuter une fois pour toutes
N = tirage(1, 1000)
message = "J'ai choisi un entier compris entre 1 et 1000. Devine-le : "
user = int(input(message))
k = 1
while user != N :
    if user < N : 
        message = "Plus grand... "
    else : 
        message = "Plus petit... "
    k = k + 1
    user = int(input(message + "Essaie encore : "))
print("\nGagné en " + str(k) + " coup(s) !")