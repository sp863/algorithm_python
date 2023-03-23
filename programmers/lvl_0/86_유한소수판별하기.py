import math

def factorize(number):
    d = 2
    output = []

    while d <= number:
        if number % d == 0:
            number /= d
            output.append(d)
        else:
            d += 1

    return output

def solution(a, b):
    gcd = math.gcd(a,b)

    den_b = b // gcd

    for num in factorize(den_b):
        if num not in [2, 5]:
            return 2
    return 1

# Solution
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

def solution(a, b):
    return 1 if a/b * 1000 % 1 == 0 else 2