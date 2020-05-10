#-------------------------------------------------------------------------------
# Name:        TP 2 - Ex 2
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     04/08/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

# 1

def isPandigi(a, b):
    c = a * b
    digits = str(c) + str(a) + str(b)
    if len(digits) != 9:
        return False
    digitsFound = [False] * 9
    for char in range(0, 9):
        digitsFound[int(digits[char]) - 1] = True
    digitIndex = 0
    allDigitFoundAtTheMoment = True
    while digitIndex < 9 and allDigitFoundAtTheMoment:
        allDigitFoundAtTheMoment = digitsFound[digitIndex]
        digitIndex += 1
    return allDigitFoundAtTheMoment

## print(isPandigi(39, 185))

# 2

## disjonction de cas

# 3

for a in range(1, 100):
    for b in range(1, 10000):
        if isPandigi(a, b):
            print("{} * {} = {}".format(a, b, a * b))