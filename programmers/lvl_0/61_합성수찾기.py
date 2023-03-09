def solution(n):
    answer = 0
    for num in range(4, n + 1):
        count = 0
        for num2 in range(1, num + 1):
            if num % num2 == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer

# Solution
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
