def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))


def factorial(n):
    multi = 1
    for num in range(1, n + 1):
        multi *= num
    return multi

# Solution
import math

def solution1(balls, share):
    return math.comb(balls, share)