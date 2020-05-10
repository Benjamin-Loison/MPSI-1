def is_div_by(nb, diviseurs):
    for diviseur in diviseurs:
        if nb % diviseur == 0: return True
    return False

def next_prime(P):
    nb = P[len(P) - 1] + 2
    while is_div_by(nb, P):
        nb += 2
    P += [nb]

def premiers(N):
    P = [2, 3]
    while P[len(P) - 1] < N:
        next_prime(P)
    
    return P[:len(P) - 1]

primes = premiers(100)    

print(primes)

def produit(N):
    primes = premiers(N)
    for width in primes:
        if N % width == 0:
            for height in primes:
                if width * height == N: return (width, height) # N % height == 0
    return (0, 0)

print(produit(21))

from os import getcwd as dir, chdir as cd

cd('U:\\')
cd('C:\\Users\\Benjamin LOISON\\Desktop\\BensFolder\\School\\CPGE\\Fenelon\\MPSI\\IPT\\19\\02\\20')
print(dir())

# print(type(octet))
# valeur = octet[0]
    
source = open('message.bin', 'rb')
octets = [source.read(1)]
while octets[len(octets) - 1] != bytes(b''):
    octets += [source.read(1)]
source.close()
octets = octets[:len(octets) - 1]
print(octets)
taille = len(octets)

binaries = []
for octet in octets:
    binaries += [octet[0]]
print(binaries)

binariesTable = []
for width in range(product[0]):
    tmp = []
    for height in range(product[1]):
        tmp += [binaries[height * product[0] + width]]
    binariesTable += [tmp]
    
print(binariesTable)

binariesTable = []
for width in range(product[1]):
    tmp = []
    for height in range(product[0]):
        tmp += [binaries[height * product[1] + width]]
    binariesTable += [tmp]

product = produit(taille)
print(product)

for i in range(product[0]):
    for j in range(product[1]):
        if binaries[i * product[1] + j]: print('X', end = '')
        else: print(' ', end = '')
    print()


for i in range(product[0] - 1,-1,-1):
    for j in range(product[1]):
        if binaries[i * product[1] + j]: print('X', end = '')
        else: print(' ', end = '')
    print()

for i in range(product[1]):
    for j in range(product[0]):
        if binaries[i * product[0] + j]: print('X', end = '')
        else: print(' ', end = '')
    print()
    
for i in range(product[1]):
    str = ""
    for j in range(product[0]):
        if binaries[i * product[0] + j]: str += 'X'
        else: str += ' '
    print(str)
    
for i in range(product[1]):
    str = ""
    for j in range(product[0]):
        if binaries[i * product[0] + j]: str += 'X'
        else: str += ' '
    if i % 2 == 0: print(str)
    else: print(str[::-1])

for i in range(product[1] - 1, -1, -1):
    for j in range(product[0]):
        if binaries[i * product[0] + j]: print('X', end = '')
        else: print(' ', end = '')
    print()

def print_line(binary_array):
    for binary in binary_array:
        if binary: print('X', end = '')
        else: print(' ', end = '')
    print()

for i in range(product[0]):
    if i % 2 == 0: print_line(binariesTable[i])
    
for i in range(product[0] -1, -1, -1):
    if i % 2 == 0: print_line(binariesTable[i])
    
for i in range(product[0]):
    if i % 2 == 0: print_line(reversed(binariesTable[i]))
    
for i in range(product[0] -1, -1, -1):
    if i % 2 == 0: print_line(reversed(binariesTable[i]))

for i in range(product[0]):
    if i % 2 == 0: print_line(binariesTable[i])
    else: print_line(reversed(binariesTable[i]))
    
for i in range(product[0]):
    if i % 2 != 0: print_line(binariesTable[i])
    else: print_line(reversed(binariesTable[i]))



for i in range(product[1]):
    if i % 2 == 0: print_line(binariesTable[i])
    
for i in range(product[1] -1, -1, -1):
    if i % 2 == 0: print_line(binariesTable[i])
    
for i in range(product[1]):
    if i % 2 == 0: print_line(reversed(binariesTable[i]))
    
for i in range(product[1] -1, -1, -1):
    if i % 2 == 0: print_line(reversed(binariesTable[i]))

for i in range(product[1]):
    if i % 2 == 0: print_line(binariesTable[i])
    else: print_line(reversed(binariesTable[i]))
    
for i in range(product[1]):
    if i % 2 != 0: print_line(binariesTable[i])
    else: print_line(reversed(binariesTable[i]))

import os
os.system("pass")