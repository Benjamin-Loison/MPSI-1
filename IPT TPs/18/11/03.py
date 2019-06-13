x = 4
test = [1, "deux", 3.0, x]
print(test)
x = 'quatre'
print(test)

a = [0, 1]
b = [2, 3]
print(a + b)
print(a * 3)

c = [0, 1, 2]
print(c[len(c)])
c + 4

# 2 a

N = 5
print(('* ' * N + '\n') * N)

# 2 b

N = 5
print('* ' * N + '\n' +
     ('*' + ' ' * ((N - 1) * 2 - 1)  + "*\n" ) * (N - 2) +
     '* ' * N + '\n')

# 2 c

N = 8
print('* ' * N)
for index in range(N - 2):
    print('*' + '  ' * index + ' *' + '  ' * (N - 3 - index) + ' *') 
print('* ' * N)

# 2 d

"""

N = 8
print('* ' * N)
for index in range(N - 2):
    line = '* '
    
    line += ' *'
print('* ' * N)

"""

N = 8
print('* ' * N)
size = N - 2
for lineIndex in range(size):
    print('* ', end = '')
    for columnIndex in range(size):
        if lineIndex == columnIndex or columnIndex == size - lineIndex - 1:
            print('* ', end = '')
        else:
            print('  ', end = '')
    print('*')
print('* ' * N)

# 3 a

size = 6
for lineIndex in range(size):
    for columnIndex in range(size):
        print(lineIndex * columnIndex, end = ' ')
    print()

# 3 b

size = 6
for lineIndex in range(size):
    for columnIndex in range(lineIndex + 1):
        print(lineIndex * columnIndex, end = ' ')
    print()

# 3 c

size = 6
for lineIndex in range(size):
    for columnIndex in range(lineIndex, size):
        print(lineIndex * columnIndex, end = ' ')
    print()

# 4

text = "This is a test string !"
toFind = ' !'
position = -1

toFindLength = len(toFind)
"""

for textIndex in range(len(text) - toFindLength + 1):
    isFound = True
    for toFindIndex in range(toFindLength):
        if toFind[toFindIndex] != text[textIndex + toFindIndex]:
            isFound = False
            break
    if isFound:
        position = textIndex
        break

"""

for textIndex in range(len(text) - toFindLength + 1):
    if text[textIndex : textIndex + toFindLength] == toFind:
        position = textIndex
        break

if position == -1:
    print("Not found")
else:
    print("Found on position: " + str(position))

# test

def test():
    print('Executed')
    return 42

for i in range(test()):
    print(i)

# 5

size = 2
for index in range(1, size + 1):
    print('* ' * index)

size = 2

'''

for lineIndex in range(1, 1 + 2 ** (size - 1)):    
    print(' ' * lineIndex)

'''

size = 5
for index in range(size):
    print((size - index - 1) * '  ' + (2 * index + 1) * '* ')

levels = 6
for levelIndex in range(2, levels):
    for index in range(0, levelIndex):
        if index == 0 and levelIndex != 2:
            print((size - levelIndex + 1) * '  ' + 'o ' + (levelIndex - 3) * '  ' + '*' + (levelIndex - 3) * '  ' + ' o')
        else:
            print((size - index - 1) * '  ' + (2 * index + 1) * '* ')