def solution(my_string):
    return sum(list(int(i) for i in my_string if i.isdigit()))