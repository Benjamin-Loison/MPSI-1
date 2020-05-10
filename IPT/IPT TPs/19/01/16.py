N = 16

def base2(nb):
    octet = []
    quotient = nb
    while quotient != 0:
        octet = [bool(quotient % 2)] + octet
        quotient //= 2
    return (N - len(octet)) * [False] + octet

print(base2(54))

def base10(octet):
    return sum([octet[-k-1] * 2 ** k for k in range(len(octet))])
    
def base10(octet):
    sum = 0
    power = 1
    octetLength = len(octet)
    for index in range(N):
        sum += octet[octetLength - index - 1] * power
        power *= 2
    return sum
    
print(base10(base2(54)))    
print(base10([True,True, False]))

# 0011 0110
# 0011 0110
# 0110 1101

# chiffre retenue
#   and/xor
#    T      F
#    F      T
#    T      T
#    T      T 

def somme_elem(R, bit0, bit1): # can be improved with up
    if bit0 and bit1 and R: return (True, True)
    elif (bit0 and bit1 and not R) or ((bit0 or bit1) and R): return (True, False)
    return (False, bit0 or bit1 or R)
    
print(somme_elem(False, False, False))
print(somme_elem(False, True, True))
print(somme_elem(True, True, True))

def somme(oct1, oct2):
    newOct = []
    R = False
    for bit0, bit1 in zip(reversed(oct1), reversed(oct2)):
        # print("bit", R, bit0, bit1, end = "\n\n")
        R, S = somme_elem(R, bit0, bit1)
        # print(R, S)
        newOct = [S] + newOct
    if R: return (N - len(newOct) - 1) * [False] + [True] + newOct
    return (N - len(newOct)) * [False] + newOct
    
print(somme(base2(54), base2(54)))
print(base10(somme(base2(54), base2(54))))

#

a = [0, 1, 2]
b = ['a', 'b', 'c']
print(list(reversed(list(zip(a, b))))) # IT WORKS

#

def complement(oct):
    # print(oct)
    newOct = []
    for bit in oct:
        newOct += [not bit]
    # print(newOct)
    oct0 = (N - len(newOct)) * [True] + newOct
    oct1 = base2(1)
    # print(oct0, oct1)
    sommeTmp = somme(oct0, oct1)
    return sommeTmp

print(complement(base2(54)))
print(base10(complement(base2(54))))
print(somme(base2(54), complement(base2(54))))
print(base10(somme(base2(54), complement(base2(54)))))

#

def multiply(oct0, oct1): return base2(base10(oct0) * base10(oct1))

print(base10(multiply(base2(4), base2(6))))

#

def valeur(oct):
    if oct[0]: return -base10(complement(oct))
    return base10(oct)

print(complement(base2(54)))
print(valeur(complement(base2(54))))
print(valeur(base2(54)))

def difference(oct1, oct2):
    return somme(oct1, complement(oct2))

print(valeur(difference(base2(54), base2(54))))
print(difference(base2(0), base2(54)) == complement(base2(54)))
print(valeur(difference(complement(base2(54)), base2(54))))

#

def multiplication(oct0, oct1):
    