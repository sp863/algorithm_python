import math

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)

    gcd = math.gcd(numer, denom)

    return [numer // gcd, denom // gcd]

# Solution
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]