import random

def makeKey(length):
    key = ""
    for i in range(length):
        digit = str(random.randint(0, 1))
        key += digit
    return key