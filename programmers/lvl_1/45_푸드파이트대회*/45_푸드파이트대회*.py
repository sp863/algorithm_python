def solution(food):
    answer = ''

    for i in range(1, len(food)):
        if food[i] // 2 > 0:
            answer += ((food[i]//2) * str(i))

    return answer + '0' + ''.join(sorted(answer, reverse=True))

# Solution


def solution(food):
    answer = "0"
    for i in range(len(food)-1, 0, -1):
        c = int(food[i]/2)
        while c > 0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer

# didn't understand the question right away...need to study other solutions
