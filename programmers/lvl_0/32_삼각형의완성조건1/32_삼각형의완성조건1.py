def solution(sides):
    return 1 if max(sorted(sides)) < sorted(sides)[0] + sorted(sides)[1] else 2

# Solution
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2