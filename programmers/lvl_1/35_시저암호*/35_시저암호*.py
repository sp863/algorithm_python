def solution(s, n):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    answer = ''

    for letter in s:
        if letter != ' ':
            if letter.isupper():
                idx = upper_letters.index(letter) + n
                if idx >= 26:
                    answer += upper_letters[idx - 26]
                else:
                    answer += upper_letters[idx]
            else:
                idx = lower_letters.index(letter) + n
                if idx >= 26:
                    answer += lower_letters[idx - 26]
                else:
                    answer += lower_letters[idx]
        else:
            answer += ' '

    return answer


# Solution

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A') + n) % 26+ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a') + n) % 26+ord('a'))

    return "".join(s)

# ord, chr are built-in functions in Python that convert a character to its ASCII value and vice versa.
