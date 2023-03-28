def solution(array):
    answer = 0
    for num in array:
        answer += str(num).count('7')
    return answer

# Solution
def solution(array):
    return str(array).count('7')