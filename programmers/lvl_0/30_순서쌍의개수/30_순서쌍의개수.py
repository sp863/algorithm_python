def solution(n):
    answer = 0

    for num in range(1, n + 1):
        if n % num == 0:
            answer += 1

    return answer

# Solution
def solution(n):
    answer =0 
    for i in range(n):
        if n % (i+1) ==0:
            answer +=1
    return answer