import collections


def solution(participant, completion):
    sorted_p = sorted(participant)
    sorted_c = sorted(completion)

    sorted_c += ['0']

    for i in range(len(participant)):
        if sorted_p[i] != sorted_c[i]:
            return sorted_p[i]

# Solution


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
