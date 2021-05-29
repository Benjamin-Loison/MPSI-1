from os import chdir as cd
from pickle import load
#from math import sqrt, exp
from math import *
from random import random
import gzip
from copy import deepcopy

#cd("C:/Users/Asus/Desktop/reg lin mnist2")
cd("C:/Users/Asus/Desktop")

ft = gzip.open('data_testing', 'rb')
TRAINING = load(ft)
OLD_TRAINING = deepcopy(TRAINING[1])
ft.close()

TMP_WORKING_ELEMENTS = 5

#NB_ELEMENTS = len(TRAINING[0])
NB_ELEMENTS = TMP_WORKING_ELEMENTS
THETA_NUMBER = int(len(TRAINING[0][0]))
SIZE = int(sqrt(THETA_NUMBER))
STEP = 0.02# / NB_ELEMENTS

theta = [0] * THETA_NUMBER
newTheta = [0] * THETA_NUMBER
#for i in range(THETA_NUMBER):
#    theta[i] = random() * NB_ELEMENTS # in order not to multiply by 0 later

for pic in range(NB_ELEMENTS): # x values here are 0 or 1, best way to prototype ?
    TRAINING[1][pic] = int(TRAINING[1][pic] != 0) # 0 for 0 and 1 for 1...9
    """for i in range(SIZE):
        for j in range(SIZE):
            if TRAINING[0][pic][i * SIZE + j]:
                TRAINING[0][pic][i * SIZE + j] = 1
            else:
                TRAINING[0][pic][i * SIZE + j] = 0"""

def mySum(picIndex):
    partialSum = 0
    for j in range(THETA_NUMBER):
        partialSum += theta[j] * TRAINING[0][picIndex][j]
    return partialSum

def h_theta(picIndex):
    partialSum = 0
    for i in range(1, THETA_NUMBER):
        partialSum += theta[i] * TRAINING[0][picIndex][i]
    return theta[0] + partialSum

#def h_theta(picIndex): # prediction
#    return 1 / (1 + mySum(picIndex))

def dh_theta(picIndex, thetaIndex):
    return TRAINING[0][picIndex][thetaIndex] / (1 + exp(-mySum(picIndex)))

"""def differenceTheta(theta0, theta1):
    sum = 0
    for i in range(THETA_NUMBER): sum += abs(theta0[i] - theta1[i])
    return sum"""

def test():
    for i in range(NB_ELEMENTS):
        print(OLD_TRAINING[i], TRAINING[1][i], h_theta(i))

for iteration in range(50):
    print(iteration)
    for i in range(THETA_NUMBER):
        sum = 0
        # if TRAINING[1][i]: continue
        for k in range(NB_ELEMENTS):
            #print(h_theta(k))
            sum += dh_theta(k, i) * (h_theta(k) - TRAINING[1][k])
        newTheta[i] = theta[i] - STEP * (sum / NB_ELEMENTS)
    #print(differenceTheta(theta, newTheta))
    for i in range(THETA_NUMBER):
        theta[i] = newTheta[i]
    test()

for i in range(SIZE):
    for j in range(SIZE):
        print(int(theta[i * SIZE + j] + 0.99), end=' ')
    print()

test()
