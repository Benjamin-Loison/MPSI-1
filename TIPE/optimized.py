from os import chdir as cd
from pickle import load
from math import sqrt, exp
from random import random
import gzip
from copy import deepcopy

#cd("C:/Users/Asus/Desktop")
cd("C:/Users/Benjamin LOISON/Desktop/BensFolder/School/CPGE/Fenelon/MPSI/TIPE/WIP/260519/old")

ft = gzip.open('data_training', 'rb')
TRAINING = load(ft)
OLD_TRAINING = deepcopy(TRAINING[1])
ft.close()

TMP_WORKING_ELEMENTS = 60000

#NB_ELEMENTS = len(TRAINING[0])
NB_ELEMENTS = TMP_WORKING_ELEMENTS
THETA_NUMBER = int(len(TRAINING[0][0]))
SIZE = int(sqrt(THETA_NUMBER))
STEP = 0.02# / NB_ELEMENTS

theta = [0] * THETA_NUMBER
newTheta = [0] * THETA_NUMBER
H_THETA = [0] * NB_ELEMENTS
E_MY_SUM = [0] * NB_ELEMENTS

for pic in range(NB_ELEMENTS): # x values here are 0 or 1, best way to prototype ?
    TRAINING[1][pic] = int(TRAINING[1][pic] != 0) # 0 for 0 and 1 for 1...9

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

def dh_theta(picIndex, thetaIndex):
    return TRAINING[0][picIndex][thetaIndex] / (1 + E_MY_SUM[picIndex])

def test():
    for i in range(NB_ELEMENTS):
        print(OLD_TRAINING[i], TRAINING[1][i], h_theta(i))

def predictionZeros():
    prediction = 0
    zeros = 0
    for i in range(NB_ELEMENTS):
        if TRAINING[1][i] == 0:
            zeros += 1
            if not bool(round(h_theta(i))):
                prediction += 1
    print((prediction / zeros) * 100, prediction, zeros)

for iteration in range(5000):
    print(iteration)
    
    for k in range(NB_ELEMENTS):
        H_THETA[k] = h_theta(k)
        E_MY_SUM[k] = exp(-mySum(k))
            
    for i in range(THETA_NUMBER):
        sum = 0
        for k in range(NB_ELEMENTS):
            sum += dh_theta(k, i) * (H_THETA[k] - TRAINING[1][k])
        newTheta[i] = theta[i] - STEP * (sum / NB_ELEMENTS)
        
    for i in range(THETA_NUMBER):
        theta[i] = newTheta[i]
        
    predictionZeros()

test()
predictionZeros()

"""

TRAINING

0
95.64409927401655 5665 5923
1
32.179638696606446 1906 5923
2
13.47290224548371 798 5923
3
9.707918284653047 575 5923
4
9.370251561708594 555 5923
5
10.332601722100287 612 5923
6

Then 11.428571428571429 112 980 on testing set

"""

"""def predictionRate():
    prediction = 0
    for i in range(NB_ELEMENTS):
        if TRAINING[1][i] == bool(round(h_theta(i))): prediction += 1
    print((prediction / NB_ELEMENTS) * 100, prediction, NB_ELEMENTS)
predictionRate()"""
