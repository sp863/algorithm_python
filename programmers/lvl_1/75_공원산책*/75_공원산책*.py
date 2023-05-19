def solution(park, routes):
    dog = []
    move_map = []
    vector = {
        'E': 1,
        'W': -1,
        'S': 1,
        'N': -1,
    }

    for i in range(len(park)):
        split_park = list(park[i])
        row = []

        for j in range(len(split_park)):
            if split_park[j] == 'S':
                dog.append(i)
                dog.append(j)
                row.append(True)
                continue
            elif split_park[j] == 'X':
                row.append(False)
                continue
            else:
                row.append(True)
                continue

        move_map.append(row)

    for i in range(len(routes)):
        route = routes[i].split(' ')
        direction = route[0]
        dist = int(route[1])

        y = dog[0]
        x = dog[1]
        for j in range(dist):
            if direction == 'E' or direction == 'W':
                x += vector[direction] * 1
            else:
                y += vector[direction] * 1

        print(y, x)

        if y < len(park) and x < len(move_map[0]) and move_map[y][x] == True:
            dog[0] = y
            dog[1] = x

    print(dog)
