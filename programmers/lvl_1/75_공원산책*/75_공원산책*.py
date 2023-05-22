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


# Solution

def solution(park, routes):
    # 위치 index
    x = 0
    y = 0

    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break

    # 이동
    for route in routes:
        # 위치 초기화
        xx = x
        yy = y
        # 이동 - 장애물이 있거나 공원을 벗어나면 명령 무시
        for step in range(int(route[2])):
            # 동쪽 : 현재 위치가 map 가장 오른쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            if route[0] == 'E' and xx != len(park[0])-1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(route[2])-1:
                    x = xx  # step만큼 움직였으면 위치 초기화
            # 서쪽 : 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'W' and xx != 0 and park[yy][xx-1] != 'X':
                xx -= 1
                if step == int(route[2])-1:
                    x = xx
            # 남쪽 : 현재 위치가 map 가장 아래쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'S' and yy != len(park)-1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(route[2])-1:
                    y = yy
            # 북쪽 : 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1
                if step == int(route[2])-1:
                    y = yy

    return [y, x]


dx = {'N': -1, 'S': 1, 'E': 0, 'W': 0}
dy = {'N': 0, 'S': 0, 'E': 1, 'W': -1}


def solution(park, routes):
    answer = []
    x, y = -1, -1
    N, M = len(park), len(park[0])
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        dir_, dist = route.split(' ')

        isFalse = False
        for i in range(1, int(dist) + 1):
            nx, ny = x + dx[dir_] * i, y + dy[dir_] * i
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                isFalse = True
                break
            if park[nx][ny] == 'X':
                isFalse = True
                break

        if isFalse:
            continue
        nx, ny = x + dx[dir_] * int(dist), y + dy[dir_] * int(dist)
        x, y = nx, ny

    answer = [x, y]

    return answer

# My solution is not working, runtime errors and other bugs. Need to study other solutions.
