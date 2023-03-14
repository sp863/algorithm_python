def solution(sides):
    sorted_sides = sorted(sides)
    short = sorted_sides[0]
    long = sorted_sides[1]

    temp1 = []
    for side in range(long - short, long + 1):
        if side + short > long:
            temp1.append(side)

    temp2 = []
    for side in range(long + 1, short + long):
        if short + long > side:
            temp2.append(side)
        else:
            break

    return len(temp1) + len(temp2)

# Solution
