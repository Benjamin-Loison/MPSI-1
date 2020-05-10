#-------------------------------------------------------------------------------
# Name:        TP 1 - Ex 1 2.
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     27/07/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

## Expected:
##
## 0
## 1
## 8
## 17
## 18
## 26
## 27

for nb in range(0, 1001):
    cube = nb ** 3
    nbStr = str(cube)
    sumDigit = 0
    for char in range(0, len(nbStr)):
        digit = int(nbStr[char])
        sumDigit += digit
    if nb == sumDigit:
        print(nb)