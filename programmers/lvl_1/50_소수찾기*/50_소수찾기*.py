def isPrime(num):
    count = 0
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n):
    return len([i for i in range(2, n + 1) if isPrime(i)])


# Solution

def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)

# this solution uses sieve of eratosthenes to find the prime numbers.
# need to understand this solution!
