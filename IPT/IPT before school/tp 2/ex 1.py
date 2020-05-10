#-------------------------------------------------------------------------------
# Name:        TP 2 - Ex 1
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     04/08/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

## a < b (a / b)

# 1

def first_denominator(a, b):
    return b // a + 1

## print(first_denominator(2, 195195))

# 2

def euclide(a, b):
    if b == 0: return a
    else: return euclide(b, a % b)

## print(euclide(21, 28))

# 3

## Ben's version doesn't work perfectly :/ (I do not have any lesson about egyptian fractions)

##def egypt_frac(a, b):
##    result = ''
##    result += str(a) + '/' + str(b) + ' = '
##    oldA = 0
##    while a != oldA: ## doesn't work perfectly with the third example
##        oldA = a
##        denominator = first_denominator(a, b)
##        result += '1/' + str(denominator) + ' + '
##        oldDenominator = b
##        b *= denominator
##        denominatorTmp = denominator
##        denominator *= oldDenominator
##        a *= denominatorTmp
##        a -= oldDenominator
##    return result
##
##print(egypt_frac(18, 121))

# correction 3

def euclide(a, b):
    if b == 0: return a
    return euclide(b, a % b)

def egypt_frac(a, b):
    ch = ''
    while a != 1:
        pgcd = euclide(a, b)
        (a, b) = (a // pgcd, b // pgcd)
        k = b // a + 1
        ch += "1/{} + ".format(k)
        (a, b) = (k*a - b, k*b)
    ch += "1/{}".format(b)
    return ch

def frac(a, b):
    print("La fraction egyptienne est: \n{}/{} = ".format(a, b), egypt_frac(a, b))

frac(12, 169)
frac(18, 121)
frac(5, 17)