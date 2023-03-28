
def solution(n):
    x = 1
    while True:
        multi = 1
        for num in range(1, x + 1):
            multi *= num
        if multi == n:
            return x
        elif multi > n:
            return x - 1
        else:
            x += 1

# Solution
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k