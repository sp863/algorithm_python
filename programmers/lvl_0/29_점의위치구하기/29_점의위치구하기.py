def solution(dot):
    x = dot[0]
    y = dot[1]

    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2 
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4

# Solution
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

def solution(dot):
    a, b = 1, 0
    if dot[0] * dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2 * a - b

def solution(dot):
    x,y = dot
    if x * y > 0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2