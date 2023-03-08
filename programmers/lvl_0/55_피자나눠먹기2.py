def solution(n):
    # n * ? % 6 = 0
    for num in range(1, (n * 6) + 1):
        if (num * n) % 6 == 0:
            return (num * n) // 6

# Solution
def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer