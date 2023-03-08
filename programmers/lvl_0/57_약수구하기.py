def solution(n):
    answer = []
    for num in range(1, n + 1):
        if n % num == 0:
            answer.append(num)
    return answer

# Solution
def solution(n):
    answer = [i for i in range(1,n+1) if n%i == 0]
    return answer