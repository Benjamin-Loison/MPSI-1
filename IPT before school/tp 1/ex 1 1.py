#-------------------------------------------------------------------------------
# Name:        TP 1 - Ex 1 1.
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     27/07/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

## n = 0; 0
## n = 1; 1
## n = 2; 3
## n = 3; 6
## n = 4; 10
## n = 5; 15

# method 0 with a for loop

def sumNb0(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum

# method 1 with a direct compute

def sumNb1(n):
    return int(n * (n + 1) / 2)

# main

# input
##n = int(input("Sum n"))

# manual
##print(sumNb0(n))
##print(sumNb1(n))

# for
for i in range(0, 6):
    print(sumNb0(i))
    print(sumNb1(i))