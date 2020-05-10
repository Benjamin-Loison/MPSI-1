#-------------------------------------------------------------------------------
# Name:        TP 1 - Ex 3
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     03/08/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

# 1

# for instance, 4 ^ 9 = 262 144 (many possibilities for Pierre) @LoveComputerPower

class Person:
    def __init__(self, name, dices, sides):
        self.name = name
        self.dices = dices
        self.sides = sides
        self.minSum = dices * 1
        self.maxSum = dices * sides
        self.arraySize = self.maxSum - self.minSum
        self.sums = [0] * (self.arraySize + 1)

    def getIndex(self, scoreSum):
        return scoreSum - self.minSum

    def displayCouple(self, index):
        print(str(index + self.minSum) + " " + str(self.sums[index]))

def computePossibilities(person, throwToDo = -1, scoreSum = 0):
    if throwToDo == -1:
        throwToDo = person.dices
    if throwToDo != 0:
        for side in range(1, person.sides + 1):
            tmpSum = scoreSum + side
            computePossibilities(person, throwToDo - 1, tmpSum)
    else:
        index = person.getIndex(scoreSum)
        person.sums[index] = person.sums[index] + 1

def computeLists(person):
    computePossibilities(person)

def displayList(person):
    for index in range(0, person.arraySize + 1):
        person.displayCouple(index)

pierre = Person("Pierre", 9, 4)
colin = Person("Colin", 6, 6)

computeLists(pierre) # first (Pierre)
## displayList(pierre)

## print()

computeLists(colin) # second (Colin)
## displayList(colin)

# 2

def proba_conda(Scolin, needPrint = True):
    global pierre
    sumAllPossibilitiesPierre = 0
    sumPossibilitiesToWinPierre = 0
    for index in range(0, pierre.arraySize + 1):
        possibilities = pierre.sums[index]
        sumAllPossibilitiesPierre += possibilities
        if index + pierre.minSum > Scolin:
            sumPossibilitiesToWinPierre += possibilities
    pourcentage = (sumPossibilitiesToWinPierre / sumAllPossibilitiesPierre) * 100
    if needPrint:
        print(str(round(pourcentage, 4)) + " %")
    else:
        return pourcentage

## proba_conda(20)

# 3

sumProbabilities = 0
lowerBound = colin.minSum
upperBound = colin.maxSum
boundSize = upperBound - lowerBound
for score in range(lowerBound, upperBound + 1):
    sumProbabilities += proba_conda(score, False)
print(sumProbabilities / boundSize)