def slope(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2

    y = y2 - y1
    x = x2 - x1

    return x / y

def solution(dots):
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1

    return 0

def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0
