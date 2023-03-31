def solution(a, b):
    return sum([num * b[idx] for idx, num in enumerate(a)])

# Solution


def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])
