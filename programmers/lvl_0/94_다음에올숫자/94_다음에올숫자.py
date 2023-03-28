def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        return common[len(common) - 1] + (common[1] - common[0])
    else:
        return common[len(common) - 1] * (common[1] // common[0])

# Solution
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)