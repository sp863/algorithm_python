def solution(numbers):
    return sum(list(set(list(range(0, 10))) ^ set(numbers)))

# Solution


def solution(numbers):
    return 45 - sum(numbers)


def solution(x): return sum(range(10)) - sum(x)


def solution(numbers):
    return sum([i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] if i not in numbers])
