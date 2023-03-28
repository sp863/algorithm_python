def pushLetters(word):
    new_word = [''] * len(word)

    for i, letter in enumerate(word):
        if i == len(word) - 1:
            new_word[0] = letter
        else:
            new_word[i + 1] = letter
    return ''.join(new_word)


def solution(A, B):
    if A == B:
        return 0

    compare_word = A

    for i in range(len(A) - 1):
        if B == pushLetters(compare_word):
            return i + 1
        compare_word = pushLetters(compare_word)

    return -1

# Solution
solution=lambda a,b:(b*2).find(a)

def solution(A, B):
    AA = A+A
    answer = AA.find(B)

    if answer >0:
        answer = len(A) - answer

    return answer