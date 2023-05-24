def solution(wallpaper):
    total_files = sum(row.count('#') for row in wallpaper)

    y = []
    x = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                y.append(i)
                x.append(j)

    return [min(y), min(x), max(y)+1, max(x)+1]

# Solution


def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]

# This solution also solved the exact same way but see how the array variables are initialized. This is possibl in python.
