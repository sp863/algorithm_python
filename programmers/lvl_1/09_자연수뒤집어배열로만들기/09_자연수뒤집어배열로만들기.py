def solution(n):
    return [int(num) for num in list(str(n)[::-1])]

# Solution
def digit_reverse(n):
    return list(map(int, reversed(str(n))))