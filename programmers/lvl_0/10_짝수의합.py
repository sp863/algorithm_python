def solution(n):
    answer = 0
    for num in range(n + 1):
        if num % 2 == 0:
            answer += num
    return answer

# Solution
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

print([i for i in range(2, 10, 2)])