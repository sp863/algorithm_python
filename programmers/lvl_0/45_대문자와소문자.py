def solution(my_string):
    answer = ''
    for letter in my_string:
        if letter.isupper():
            answer += letter.lower()
        else:
            answer += letter.upper()

    return answer

# Solution
def solution(my_string):
    return my_string.swapcase()