def solution(n, k):
    return n * 12000 + k * 2000 - ((n // 10) * 2000)

# Solution
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)