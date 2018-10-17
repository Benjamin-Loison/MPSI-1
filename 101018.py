# 1.a

n = 42
u = 0

for k in range(n):
    u += 1
    
print(u)

# 1.b

n = 4
a = 3
u = 1

for k in range(n):
    u *= a
    
print(u)

# 1.c

n = 4
a = 3
u = a

for k in range(n):
    # Un+1 = Un ^ a
    u = u ** a ## u power a
    
print(u)

# 1.d

n = 2
a = 3
u = a
for k in range(n):
    u = a ** u

print(u)

# 2.a

n = 4
print(("* " * n + "\n") * n)

# 2.b

n = 7
print("* " * n)
for k in range(n - 2):
    print("* " + " " * (2 * n - 5) + " *")
print("* " * n)

# without spaces 1

n = 42
upperLimit = n - 2
print("* " * n)
for k in range(upperLimit):
    print("* " + "+" * (2 * n  - 5) + " *")
print("* " * n)

# without spaces 2

n = 9
upperLimit = n - 2
print("* " * n)
for k in range(upperLimit):
    print("* " + "  " * upperLimit + "*")
print("* " * n)

# 2.c

# 1

n = 5
print("* " * n)
for k in range(n - 2):
    print("* " + " " * (2 * k) + "*" + " " * (2 * n - 6 - 2 * k) + " *")
print("* " * n)

# 2

n = 7
upperLimit = n - 2
print("* " * n)
for k in range(upperLimit):
    print("* " + "  " * k + "+" + "  " * (upperLimit - k - 1) + " *")
print("* " * n)

# 3.a

columnsNumber = 8
linesNumber = 7
for lineIndex in range(linesNumber):
    lign = ""
    for columnIndex in range(columnsNumber):
        lign += str(columnIndex * lineIndex) + " "
    print(lign)

# 3.b

columnsNumber = 8
linesNumber = 7
for lineIndex in range(linesNumber):
    lign = ""
    for columnIndex in range(lineIndex + 1):
        lign += str(columnIndex * lineIndex) + " "
    print(lign)

# 3.c

columnsNumber = 7
linesNumber = 6
for lineIndex in range(linesNumber):
    lign = ""
    for columnIndex in range(lineIndex, linesNumber):
        lign += str(columnIndex * lineIndex) + " "
    print(lign)

# 4

# 1

text = "This is a test string"
word = "test"
position = -1

for positionIndex in range(len(text)):
    charCorrect = True
    charIndex = 0
    while charCorrect and charIndex < len(word):
        if text[positionIndex + charIndex] != word[charIndex]:
            charCorrect = False
        charIndex += 1
    if charIndex == len(word):
        position = positionIndex

if position == -1:
    print("Not found")
else:
    print("Found at: " + str(position))

# 2

text = "This is a test string !"
word = " !"
position = -1
positionIndex = 0

while position == -1 and positionIndex < len(text):
    charCorrect = True
    charIndex = 0
    while charCorrect and charIndex < len(word):
        if text[positionIndex + charIndex] != word[charIndex]:
            charCorrect = False
        charIndex += 1
    if charIndex == len(word):
        position = positionIndex
    positionIndex += 1

if position == -1:
    print("Not found")
else:
    print("Found at: " + str(position))

# 3

text = "This is a test string !"
word = "test"
position = -1

for positionIndex in range(len(text)):
    charCorrect = True
    for charIndex in range(len(word)):
        if positionIndex + charIndex < len(text):
            if text[positionIndex + charIndex] != word[charIndex]:
                charCorrect = False
    if charCorrect:
        position = positionIndex

if position == -1:
    print("Not found")
else:
    print("Found at: " + str(position))

# 4

text = "This is a test string !"
word = "test"
position = -1

for positionIndex in range(len(text) - len(word) + 1):
    if word == text[positionIndex : positionIndex + len(word)]:
        position = positionIndex
        break

if position == -1:
    print("Not found")
else:
    print("Found at: " + str(position))

# 5

n = 7
middle = n
for k in range(n):
    sideSpaces = middle - k - 1
    print(sideSpaces * "  " + "* " * (2 * k + 1) + "  " * sideSpaces)

levels = 4
for n in range(levels)
