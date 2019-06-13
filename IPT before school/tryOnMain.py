#-------------------------------------------------------------------------------
# Name:        TryOnMain
# Purpose:     Training
#
# Author:      Benjamin Loison
#
# Created:     04/08/2018
# Copyright:   (c) Benjamin Loison 2018
# Licence:     Quote the author
#-------------------------------------------------------------------------------

##import math
##import matplotlib.pyplot as plt
##import numpy as np
##from mpl_toolkits.mplot3d import Axes3D
##
##x = [1., 2.5, 4.]
##y = [3., 1., 5.]
##plt.axis('equal')
##plt.plot(x, y)
##plt.axis([-1., 5., -1., 6.])
##plt.grid()
##plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.arccos((1-x)/(1+x))+np.arcsin(2*x**(1/2)/(1+x))

X=np.linspace(0, 2, 100)
plt.plot(X, f(X))
plt.show()

"""

cubeCounter = 0

for floorIndex in range(1, 19, 2):
    cubeCounter += floorIndex ** 3
    print(floorIndex, floorIndex ** 3)

print(cubeCounter)