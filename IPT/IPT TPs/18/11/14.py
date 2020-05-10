endroit = 'palindrome'
print(endroit[len(endroit) + 1: -1 : -1])
print(endroit[len(endroit) : 0 : -1])
print(list(range(len(endroit), 0, -1)))
print(endroit[list(range(len(endroit), 0, -1))])
print(endroit[range(len(endroit), 0, -1)])
print('abcd'[:: -1])
a = 'ee'
str


import time

def test():
    print("exec")
    return ['a', 'b', 'c']

i = 0
for i in test():
    print(i)

while test():
    print("a")
    time.sleep(2)
    
l = []
val = 1
N = 128
while val <= N:
    l += [val]
    val *= 2
print(l)

l = [1]
N = 128
while l[len(l) - 1] < N:
    l += [l[len(l) - 1] * 2]
print(l)