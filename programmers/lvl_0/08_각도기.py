def solution(angle):
    if angle < 90 and angle > 0:
        return 1
    if angle == 90:
        return 2
    if angle < 180 and angle > 90:
        return 3
    if angle == 180:
        return 4

# Solution
def solution(angle):
    if angle<=90:
        return 1 if angle < 90 else 2
    else:
        return 3 if angle < 180 else 4

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer