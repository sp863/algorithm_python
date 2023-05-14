def solution(survey, choices):
    answer = ''
    benchmark = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }

    for surv, choice in zip(survey, choices):
        if choice < 4:
            benchmark[surv[0]] += (4 - choice)
        elif choice > 4:
            benchmark[surv[1]] += (choice - 4)

    b_list = list(benchmark.items())

    for i in range(0, 8, 2):
        if b_list[i][1] < b_list[i + 1][1]:
            answer += b_list[i + 1][0]
        else:
            answer += b_list[i][0]

    return answer

# Solution


def solution(survey, choices):
    answer = ''
    RTCFJMAN = [0, 0, 0, 0, 0, 0, 0, 0]
    str = "RTCFJMAN"
    for i in range(len(survey)):
        RTCFJMAN[str.index(survey[i][1])] += choices[i]-4

    if (RTCFJMAN[0] >= RTCFJMAN[1]):
        answer += "R"
    else:
        answer += "T"
    if (RTCFJMAN[2] >= RTCFJMAN[3]):
        answer += "C"
    else:
        answer += "F"
    if (RTCFJMAN[4] >= RTCFJMAN[5]):
        answer += "J"
    else:
        answer += "M"
    if (RTCFJMAN[6] >= RTCFJMAN[7]):
        answer += "A"
    else:
        answer += "N"

    return answer


def solution(survey, choices):

    my_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    for A, B in zip(survey, choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

# Need to study this problem again. Different ways to create a dictionary like object for gathering scores.
