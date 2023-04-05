def solution(array, commands):
    answer = []

    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])

    return answer

# Solution


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# map 사용하는 방법을 배울 수 있음
