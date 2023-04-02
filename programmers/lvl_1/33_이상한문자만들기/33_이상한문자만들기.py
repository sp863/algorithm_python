def solution(s):
    to_lower = s.lower()
    answer = ''

    for word in to_lower.split(' '):
        temp = ''
        for idx, letter in enumerate(word):
            if idx % 2 == 0:
                temp += letter.upper()
            else:
                temp += letter
        answer += temp
        answer += ' '

    return answer[:-1]

# Solution


def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
