def solution(n, m, section):
    paint, answer = section[0]-1, 0

    for v in section:
        if paint < v:
            paint = v + m - 1
            answer += 1

    return answer

# Solution


def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer

# Solution review needed
