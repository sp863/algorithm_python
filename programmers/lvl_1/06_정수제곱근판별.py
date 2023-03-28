import math

def solution(n):
    squared = math.sqrt(n)
    return (squared + 1) ** 2 if squared % 1 == 0 else -1

# Solution
def nextSqure(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2

def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'