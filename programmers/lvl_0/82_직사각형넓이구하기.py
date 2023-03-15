def solution(dots):
    x_coords = []
    width = 0

    for dot in dots:
        if dots[0][0] == dot[0]:
            x_coords.append(dot)
        else:
            width = abs(dots[0][0] - dot[0])

    height = abs(x_coords[0][1] - x_coords[1][1])

    return height * width

# Solution
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])