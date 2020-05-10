#-------------------------------------------------------------------------------
# Name:        TP 1 - Ex 2
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     27/07/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

from random import randint

inputMessage = "Your MasterMind choice (4 digits between 0 and 8, both included)"
gameEnded = False
lineGenerated = ""
lineUser = ""

def initialize():
    global lineGenerated
    for char in range(0, 4):
        lineGenerated += str(randint(0, 8))
    # print("Need to find: " + lineGenerated)

def checkMasterMindInput(line):
    if(len(line) != 4):
        return False
    for char in range(0, 4):
        digit = int(line[char])
    if(digit == 9):
        return False
    return True

def failDetails():
    global lineUser, lineGenerated
    wellPut = 0
    notWellPut = 0 ## good digit used in a wrong place
    for char in range(0, 4):
        if lineUser[char] == lineGenerated[char]:
            wellPut += 1
        else:
            for charOtherPlace in range(0, 4):
                if char != charOtherPlace:
                    if lineUser[char] == lineGenerated[charOtherPlace] and lineUser[charOtherPlace] != lineGenerated[charOtherPlace]:
                        notWellPut += 1
                        break
    print(lineUser + " : " + str(wellPut) + " well put " + str(notWellPut) + " not well put")
    lineUser = ""

def endGame():
    global gameEnded, lineUser
    gameEnded = True
    print("You found the generated MasterMind choice: " + lineUser + " congratulations !")

# main code

initialize()
while not gameEnded:
    while not checkMasterMindInput(lineUser):
        lineUser = input(inputMessage)
    if lineGenerated == lineUser:
        endGame()
    else:
        failDetails()