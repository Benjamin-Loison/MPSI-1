def is_in(nb, L):
    for element in L:
        if nb == element:
            return True
    return False

##

def regime(L):
    list = []
    for element in L:
        if not is_in(element, list):
            list += [element]
    return list

obelix = ["sanglier", "oie", "sanglier", "perdrix", "oie", "sanglier"]
asterix = regime(obelix)
print(obelix, asterix)

##

def doublon(element, L):
    firstIndex = -1
    for index in range(len(L)):
        if element == L[index]:
            if firstIndex != -1:
                return firstIndex
            firstIndex = index
    return firstIndex

test = [0, 1, 0, 4, 3, 4]

def doublon(nb, L):
    #if not is_in(nb, L):
    #    return False
    for index in range(len(L)):
        if nb == L[index]:
            # print(index, nb, L[index + 1:])
            if is_in(nb, L[index + 1:]):
                return index
            return -1
    return -1

print(doublon(2, test), doublon(1, test), doublon(4, test))

##

def suppr(i, L):
    return L[:i] + L[i + 1:]
    
##

obelix = ["sanglier", "oie", "sanglier", "perdrix", "oie", "sanglier"]

def liposuccion(L):
    index = 0
    while index < len(L):
        element = L[index]
        removeIndex = doublon(element, L)
        if removeIndex != -1:
            L[:] = suppr(removeIndex, L)
        index += 1

liposuccion(obelix)
print(obelix)

##

def is_in(nb, L):
    for element in L:
        if nb < element:
            return False
        if nb == element:
            return True
    return False

##

500


250


125


62

63


31 (62 and half 63)

32 (half 63)

##

def is_in(nb, L):
    length = len(L)
    middle = length // 2
    if nb < L[0] or nb > L[length - 1]: return False
    if nb == L[middle]: return True
    if nb < L[middle]: return is_in(nb, L[:middle])
    return is_in(nb, L[middle + 1:])

#

MAX_LIST_LENGTH = 6
NUMBER_POSSIBILITIES = range(10)

allCombinations = []

#

list from range to generate all number possibilities

#

def fillList(L, index, listLength):
    global allCombinations
    if index > listLength:
        allCombinations += [L]
    else:
        for char in NUMBER_POSSIBILITIES:
            fillList(L + [char], index + 1, listLength)

for listLength in range(MAX_LIST_LENGTH):
    fillList([], 0, listLength)

print(allCombinations)

#for list in allCombinations:
#    print(list)

#

def isSorted(L):
    for index in range(len(L) - 1):
        if L[index] > L[index + 1]:
            return False
    return True

allCombinationsSorted = []
for list in allCombinations:
    if isSorted(list):
        allCombinationsSorted += [list]

print(allCombinationsSorted)

for list in allCombinations:
    for nb in NUMBER_POSSIBILITIES:
        # print(list, nb, (nb in list) == is_in(nb, L))
        if nb in list:
            if not is_in(nb, list):
                print(list, nb) # with first is_in: everything's fine
            #print(list, nb, is_in(nb, list)) # with second is_in: many fails (normal behaviour)
            
for list in allCombinationsSorted:
    for nb in NUMBER_POSSIBILITIES:
        # print(list, nb, (nb in list) == is_in(nb, L))
        if nb in list:
            if not is_in(nb, list):
                print(list, nb) # with first is_in: everything's fine
            #print(list, nb, is_in(nb, list))

for list in allCombinationsSorted:
    for nb in NUMBER_POSSIBILITIES:
        if (nb in list) != is_in(nb, list):
            print(list, nb, nb in list, is_in(nb, list))