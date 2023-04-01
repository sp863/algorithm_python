def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()

    return False

# Solution


def alpha_string46(s):
    return s.isdigit() and len(s) in [4, 6]

# read the question carefully and boolean values can be returned directly
