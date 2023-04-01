import math


def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd
    return [gcd, lcm]

# Solution


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer


def solution(n, m):
    def gcd(a, b): return b if not a % b else gcd(b, a % b)
    def lcm(a, b): return a*b//gcd(a, b)
    return [gcd(n, m), lcm(n, m)]
