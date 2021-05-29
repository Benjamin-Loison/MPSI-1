from os import chdir as cd
from pickle import load
from math import sqrt, exp
from random import random
import gzip
from copy import deepcopy

# exposé dans environ15 jours

cd("C:/Users/Asus/Desktop")
#cd("C:/Users/Benjamin LOISON/Desktop/BensFolder/School/CPGE/Fenelon/MPSI/TIPE/WIP/260519/old")

ft = gzip.open('data_testing', 'rb')
TRAINING = load(ft)
OLD_TRAINING = deepcopy(TRAINING[1])
ft.close()

TMP_WORKING_ELEMENTS = 600

#NB_ELEMENTS = len(TRAINING[0])
NB_ELEMENTS = TMP_WORKING_ELEMENTS
THETA_NUMBER = int(len(TRAINING[0][0]))
SIZE = int(sqrt(THETA_NUMBER))
STEP = 0.02 / NB_ELEMENTS

theta = [[0] * THETA_NUMBER for i in range(10)]
newTheta = [[0] * THETA_NUMBER for i in range(10)]
H_THETA = [[0] * NB_ELEMENTS for i in range(10)]
E_MY_SUM = [[0] * NB_ELEMENTS for i in range(10)]

def mySum(picIndex, numberIndex):
    partialSum = 0
    for j in range(THETA_NUMBER):
        partialSum += theta[numberIndex][j] * TRAINING[0][picIndex][j]
    return partialSum

def h_theta(picIndex, numberIndex):
    partialSum = 0
    for i in range(1, THETA_NUMBER):
        partialSum += theta[numberIndex][i] * TRAINING[0][picIndex][i]
    return theta[numberIndex][0] + partialSum

def dh_theta(picIndex, thetaIndex, numberIndex):
    return TRAINING[0][picIndex][thetaIndex] / (1 + E_MY_SUM[numberIndex][picIndex])

def prediction(index):
    bestIndex = -1
    bestDistance = 10 # "largest" distance
    for numberIndex in range(10):
        hTet = h_theta(index, numberIndex)
        if abs(hTet - 1) < 0.5:
            distance = abs(hTet - 1)
        else:
            distance = abs(hTet)
        if distance < bestDistance:
            bestIndex = numberIndex
            bestDistance = distance
    return bestIndex

def predictionRate():
    nb = 0
    for i in range(NB_ELEMENTS):
        if OLD_TRAINING[i] == prediction(i): nb += 1
    print((nb / NB_ELEMENTS) * 100, nb, NB_ELEMENTS)

def predictionIndex(index, debug = False):
    prediction = 0
    nbIndex = 0
    for i in range(NB_ELEMENTS):
        if OLD_TRAINING[i] == index:
            nbIndex += 1
            if not bool(round(h_theta(i, index))):
                prediction += 1
    if debug: return prediction, nbIndex
    return prediction
            

for numberIndex in range(10):
    print(numberIndex)
    for pic in range(NB_ELEMENTS):
        TRAINING[1][pic] = int(OLD_TRAINING[pic] != numberIndex)

    iteration = 0
    lastValue = NB_ELEMENTS
    predi = predictionIndex(numberIndex)
    lastImprove = 0
    while predi <= lastValue and lastImprove < 2:
        if predi == lastValue: lastImprove += 1
        else: lastImprove = 0
        for i in range(10): print(predictionIndex(i, True))
        lastValue = predi
        print("it", iteration, predi)
        
        for k in range(NB_ELEMENTS):
            H_THETA[numberIndex][k] = h_theta(k, numberIndex)
            E_MY_SUM[numberIndex][k] = exp(-mySum(k, numberIndex))
                
        for i in range(THETA_NUMBER):
            sum = 0
            for k in range(NB_ELEMENTS):
                sum += dh_theta(k, i, numberIndex) * (H_THETA[numberIndex][k] - TRAINING[1][k])
            newTheta[numberIndex][i] = theta[numberIndex][i] - STEP * sum
        
        for i in range(THETA_NUMBER):
            theta[numberIndex][i] = newTheta[numberIndex][i]
        iteration += 1
        predi = predictionIndex(numberIndex)

predictionRate()
