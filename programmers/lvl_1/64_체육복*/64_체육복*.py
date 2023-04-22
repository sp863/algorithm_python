def solution(n, lost, reserve):
    answer = 0
    reserve.sort()
    temp = reserve[:]

    for i in reserve:
        if i in lost:
            lost.remove(i)
            temp.remove(i)
    reserve = temp[:]

    for i in reserve:
        if lost:
            if i-1 in lost:
                lost.remove(i-1)
            elif i+1 in lost:
                lost.remove(i+1)
        else:
            break

    answer = n - len(lost)
    return answer

# Solution


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# need review
