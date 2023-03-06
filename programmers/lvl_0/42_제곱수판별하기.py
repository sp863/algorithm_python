def solution(n):
    for num in range(1, n):
        if num * num == n:
            return 1

    return 2

# Solution
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2