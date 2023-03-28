def solution(n, t):
    x = 0
    sum = n

    while x < t:
        sum = sum * 2
        x += 1

    return sum

# Solution
def solution(n, t):
    answer = 2**t * n
    return answer
