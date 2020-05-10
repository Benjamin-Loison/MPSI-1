def test():
    """This is a documentation. """
    pass
    
help(test)

#

def sum(a, b):
    global test
    test = a + b
sum(1, 2)
print(test)

#

def disp(a, b):
    print("a: " + str(a))
    print("b: " + str(b))

disp(b = 42, a = 7)

#

def foo(*args):
    for a in args:
        print(a)

foo(1)
print()
foo(1,2,3)

#

def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])

bar(name='one', age=27)

#

print(4 // 2)
print(4 / 2)

##

print(3.14)

##

print(print)
print(foo)

##

print(type(foo))
# returns <class 'function'>

##

def triangle(size, car):
    for i in range(1, size + 1):
        print(car * i)

i = 1
for car in "str":
    triangle(3+i, car)
    i += 2
    
# "this is ugly"
# -> use zip

##

def triangle(size, car):
    for i in range(1, size + 1):
        print(car * i)

chars = "str"
indexes = range(1, 25, 2) # over chars length doesn't care

# Two iterables are passed
result = zip(chars, indexes)
# Converting itertor to set
resultSet = set(result)
# print(type(result)) # returns zip
# print(type(resultSet)) # returns set
# print(resultSet)
for setIndex in resultSet:
    # print(type(setIndex)) # returns tuple
    triangle(3 + setIndex[1], setIndex[0])

##

def load():
    global a # no global a = 2 (doesn't work)
    a = 2

load()
print(a)

##

def val_abs(x):
    if x < 0:
        return -x
    return x
    
##

def isIn(val, L):
    for case in L:
        if case == val:
            return True
    return False

##

