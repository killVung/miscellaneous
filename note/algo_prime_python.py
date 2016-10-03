'''
Write a program to check whether the number "n" is a prime number
'''
from math import sqrt
def isPrime(n):
    if n == 2:
        return True
    elif n >= 2 and n % 2 == 0:
        return False

    for i in range(3,int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
