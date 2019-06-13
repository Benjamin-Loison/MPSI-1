testStr = "abcdef"
print(testStr[::-2])
print(testStr[:-7])

print((type((2)j)))
print("" in "abc")

L = ["a", 'b', 42]
capsule = [7]
L += [capsule]
print(L)

capsule[0] = "gen"
print(L)

s = "abc"

def jean():
    s = "dce"
    pass

jean()
print(s)

L = [1, 2, 3, 4]
L2 = L + [5] ; print(L2)
L[0] = 'bouh' ; print(L) ; print(L2)

L = [1, 2, 3, 4]
L3 = L + []
L[0] = 'a'
print(L, L3)

print()



L = 6*[0] ; L
M = 4*[L] ; print(M)

M = [[0]*6]*4 ; print(M)

M = []
for i in range(4) :
    M += [[0]*6]
print(M)

M[3][5] = 1

for i in range(,10,2): # doesn't work
    print(i)
    
from PIL import Image as img

def disp(path):
    file = img.open(path)
    file.show()

disp("C:/Users/Benjamin LOISON/Desktop/BensFolder/School/CPGE/Fenelon/MPSI/IPT/19/3/20/1.pgm");