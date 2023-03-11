def solution(my_string):
    temp = ''
    for x in my_string:
        if not x.isdigit():
            temp += '-'
        else:
            temp += x

    return sum([int(num) for num in temp.split('-') if num.isdigit()])

# Solution -> treats whitespace as one when using split() without any arguments
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())