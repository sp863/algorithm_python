def solution(my_string, num1, num2):
    list_str = list(my_string)
    temp = list_str[num1]
    list_str[num1] = list_str[num2]
    list_str[num2] = temp
    return ''.join(list_str)

# Solution
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)