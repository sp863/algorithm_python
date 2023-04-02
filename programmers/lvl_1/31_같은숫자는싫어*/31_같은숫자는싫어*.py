def solution(arr):
    arr += ['x']
    answer = []
    prev = arr[0]
    for num in arr:
        if num != prev:
            answer.append(prev)
            prev = num

    return answer

# Solution


def solution1(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a
