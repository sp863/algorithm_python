def solution(s):
    alpha = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']
    if s.isdigit():
        return int(s)

    for i in range(len(alpha)):
        if alpha[i] in s:
            s = s.replace(alpha[i], str(i))

    return int(s)


# Solution

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
