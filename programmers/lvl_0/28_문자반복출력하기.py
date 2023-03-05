def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += (char * n)
    return answer

# Solution
def solution(my_string, n):
    return ''.join(i * n for i in my_string)