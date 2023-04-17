def solution(X, Y):
    zx = [0] * 10
    zy = [0] * 10

    for x in X:
        zx[int(x)] += 1

    for y in Y:
        zy[int(y)] += 1

    answer = ''

    for i in range(9, -1, -1):
        answer += str(i) * min(zx[i], zy[i])

    if len(answer) == 0:
        return '-1'

    if answer[0] == '0':
        return '0'

    return answer

# Solution


def solution(X, Y):
    answer = ''

    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer

# need review
