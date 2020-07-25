import sys

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)    

try:
    x = int(sys.argv[1])
except TypeError as err:
    print("Incorrect type of argument!\n")

print(factorial(x))
