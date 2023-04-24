def solution(s):
    cnt1 = 0
    cnt2 = 0
    x = s[0]
    answer = 0

    for index, letter in enumerate(s):
        if letter == x:
            cnt1 += 1
        if letter != x:
            cnt2 += 1

        if cnt1 == cnt2:
            answer += 1
            cnt1 = 0
            cnt2 = 0

            if index + 1 < len(s):
                x = s[index+1]

    if cnt1 > 0 or cnt2 > 0:
        answer += 1

    return answer

# Solution


def solution(s):
    answer = 0
    sav1 = 0
    sav2 = 0
    for i in s:
        if sav1 == sav2:
            answer += 1
            a = i
        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    return answer

# this solution doesn't need to calculate what's left after counting different letters
