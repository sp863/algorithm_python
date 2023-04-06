def solution(s):
    location = {}
    answer = []

    for i in range(len(s)):
        if f"{s[i]}" in location:
            answer.append(i - location[f"{s[i]}"])
            location[f"{s[i]}"] = i
        else:
            answer.append(-1)
            location[f"{s[i]}"] = i

    return answer

# Solution


def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer

# solution uses the oppsoite condition from mine
