from itertools import combinations


def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i + 1, len(number)-1):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

# Solution


def solution(number):
    answer = 0
    l = len(number)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
    return answer


def solution(number):
    cnt = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            cnt += 1
    return cnt
