def solution(n):
    answer = ''
    while n > 0:
        quot, remain = divmod(n, 3)
        n = quot
        answer += str(remain)

    return sum([int(value) * (3 ** idx) for idx, value in enumerate(answer[-1::-1])])

# Solution


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


# use int function to change x base string number to 10 base integer
