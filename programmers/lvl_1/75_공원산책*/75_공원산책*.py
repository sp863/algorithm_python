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
        can_move = True
        for j in range(dist):
            if direction == 'E' or direction == 'W':
                move = x + vector[direction]
                if move < len(move_map[0]) and move_map[y][move] == True:
                    x = move
                else:
                    can_move = False
            else:
                move = y + vector[direction]
                if move < len(park) and move_map[move][x] == True:
                    y = move
                else:
                    can_move = False

        if can_move == True:
            dog[0] = y
            dog[1] = x

    return dog
