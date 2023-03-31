def solution(s):
    half_point = len(s) // 2
    return s[half_point] if len(s) % 2 != 0 else s[half_point-1:half_point+1]

# Solution


def string_middle(str):
    return str[(len(str)-1)//2: len(str)//2 + 1]
