def solution(s):
    p_count = s.count('p') + s.count('P')
    y_count = s.count('y') + s.count('Y')

    return True if p_count == y_count else False

# Solution
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')