def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

# Solution


def solution(mylist):
    return [i for i in mylist if i > min(mylist)]
