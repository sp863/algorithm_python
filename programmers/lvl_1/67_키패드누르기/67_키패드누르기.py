def solution(numbers, hand):
    key_pad = [['1', '2', '3'], ['4', '5', '6'],
               ['7', '8', '9'], ['*', '0', '#']]
    left_click = '147'
    right_click = '369'

    hand_loc = {}

    for i in range(len(key_pad)):
        for j in range(len(key_pad[i])):
            hand_loc[key_pad[i][j]] = (i, j)

    left_thumb = (3, 0)
    right_thumb = (3, 2)
    answer = ''

    for num in numbers:
        y, x = hand_loc[f"{num}"]

        if x == 0:
            answer += 'L'
            left_thumb = (y, x)
        elif x == 2:
            answer += 'R'
            right_thumb = (y, x)
        else:
            ly, lx = left_thumb
            ry, rx = right_thumb

            distL = abs(y - ly) + abs(x - lx)
            distR = abs(y - ry) + abs(x - rx)

            if distL < distR:
                answer += 'L'
                left_thumb = (y, x)
            elif distR < distL:
                answer += 'R'
                right_thumb = (y, x)
            else:
                if hand == 'left':
                    answer += 'L'
                    left_thumb = (y, x)
                else:
                    answer += 'R'
                    right_thumb = (y, x)

    return answer

# Solution


def solution(numbers, hand):
    answer = ''
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

# Didn't understand the problem at first try...solution is easier cuz it just assigns the key rather than a coordinate
