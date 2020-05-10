## I

from os import getcwd
from os import chdir

print(getcwd())
chdir("C:\\Users\\bloison\\Desktop")
print(getcwd())

## II

# line by line lettre.txt

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("lettre.txt", "r")
for line in file:
    print(line)
file.close()

# one for two

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("lettre.txt", "r")
needPrint = True
for line in file:
    if needPrint: print(line)
    needPrint = not needPrint
file.close()

# line by line dialogue.txt

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("dialogue.txt", "r")
for line in file:
    print(line)
file.close()

## HP: display first two lines

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("dialogue.txt", "r")
print(file.readline())
print(file.readline())
file.close()

## reversed dialogue.txt

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("dialogue.txt", "r")
lines = file.readlines()
for lineIndex in range(len(lines) - 1, -1, -1):
    print(lines[lineIndex])
file.close()

## III

# failed try

import os

os.chdir("C:\\Users\\bloison\\Downloads")

linesNumber = 0
file = open("mystere.txt", "r")
for line in file:
    linesNumber += 1
    if line != '\n':
        print(line)

print("linesNumber:", linesNumber) # 52
file.close()

## print mystere.txt

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("mystere.txt", "r")
line = file.readline()
while line == '\n':
   line = file.readline()
print(line)

file.close()

## display Mona Lisa

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("mystere.txt", "r")
line = file.read(1)
while line == '\n':
    line = file.read(1)
    
line += file.read(67)
while line != '':
    print(line)
    line = file.read(68)
print(line)

file.close()

# failed try

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("mystere.txt", "r")
for line in range(51):
    file.readline()

line = file.read(68)
while 
print(file.read(68))

file.close()

## export Mona Lisa with linesNumber as known

import os

os.chdir("C:\\Users\\bloison\\Downloads")

writeFile = open("tableau.txt", "w")
file = open("mystere.txt", "r")
for lineIndex in range(51):
    file.readline()

line = file.read(68)
while line != '':
    #print(line)
    writeFile.write(line + '\n')
    line = file.read(68)

writeFile.write(line + '\n')

writeFile.close()
file.close()

## export Mona Lisa without knowing linesNumber

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("mystere.txt", "r")
writeFile = open("tableau.txt", 'w')
line = file.read(1)
while line == '\n':
    line = file.read(1)
    
line += file.read(67)
while line != '':
    writeFile.write(line + '\n')
    line = file.read(68)
writeFile.write(line)

writeFile.close()
file.close()

## 3

import os

os.chdir("C:\\Users\\bloison\\Downloads")

file = open("mystere.txt", "r")
for lineIndex in range(50):
    file.readline()

line = file.readline()
file.read(68)
for lineIndex in range(50):
    print(line)
    file.read(2)
    line = file.read(64)
    file.read(2)

file.close()

## II

import os

os.chdir("C:\\Users\\bloison\\Downloads")

def upperCase(source, target):
    sourceFile = open(source, "r")
    targetFile = open(target, "w")
    char = sourceFile.read(1)
    while char != '':
        charOrd = ord(char)
        if 97 <= charOrd <= 122: targetFile.write(chr(charOrd - 32))
        else: targetFile.write(char)
        char = sourceFile.read(1)
    sourceFile.close()
    targetFile.close()

upperCase("lettre.txt", "lettreUp.txt")

## 1

import os

os.chdir("C:\\Users\\bloison\\Downloads")

sourceFile = open("lettre.txt", "r")
char = sourceFile.read(1)
while char != '':
    print(char)
    char = sourceFile.read(1)
sourceFile.close()

## 2

import os

os.chdir("C:\\Users\\bloison\\Downloads")

sourceFile = open("lettre.txt", "r")
targetFile = open("maj.txt", "w")
char = sourceFile.read(1)
while char != '':
    targetFile.write(char)
    # print(char)
    char = sourceFile.read(1)
sourceFile.close()
targetFile.close()

## 3

def maj(char):
    charOrd = ord(char)
    if 97 <= charOrd and charOrd <= 122: return chr(charOrd - 32)
    return char

print(maj('h'))
print(maj('é'))

## 4

import os

os.chdir("C:\\Users\\bloison\\Downloads")

def maj(char):
    charOrd = ord(char)
    if 97 <= charOrd and charOrd <= 122: return chr(charOrd - 32)
    return char

def convertir(source, cible):
    sourceFile = open(source, "r")
    targetFile = open(cible, "w")
    char = sourceFile.read(1)
    while char != '':
        targetFile.write(maj(char))
        # print(maj(char))
        char = sourceFile.read(1)
    sourceFile.close()
    targetFile.close()
    
convertir("lettre.txt", "maj.txt")

## display Mona Lisa (permanent) 1

import os
import time

os.chdir("C:\\Users\\bloison\\Downloads")

i = 0
while True:

    file = open("mystere.txt", "r")
    line = file.read(1)
    while line == '\n':
        line = file.read(1)

    time.sleep(0.01)
    file.read(i)
    i += 1
    if i == 68: i = 0
    line += file.read(67)
    while line != '':
        print(line)
        line = file.read(68)
    print(line)

file.close()

## display Mona Lisa (permanent) 2

import os
import time

os.chdir("C:\\Users\\bloison\\Downloads")


def nextIteration():
    for linesIndex in range(linesLength):
        lines[linesIndex] = lines[linesIndex][-1] + lines[linesIndex][:-1] 

file = open("paint.txt", "r")

lines = file.readlines()
linesLength = len(lines)
for linesIndex in range(linesLength):
    lines[linesIndex] = lines[linesIndex][:-1]
    
file.close()

while True:
    total = ""
    for line in lines:
        total += line + '\n'
    print(total)
    time.sleep(0.1)
    nextIteration()