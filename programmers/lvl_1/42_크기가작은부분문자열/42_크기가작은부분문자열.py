def solution(t, p):
    count = 0

    for i in range(len(t)):
        number = ''
        for j in range(i, i + len(p)):
            if j < len(t):
                number += t[j]
        if len(number) == len(p) and int(number) <= int(p):
            count += 1

    return count

# Solution


def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1

    return answer
