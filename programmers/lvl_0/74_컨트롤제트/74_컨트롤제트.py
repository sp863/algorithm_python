def solution(s):
    zArr = s.split()
    sum = 0

    for i, num in enumerate(zArr):
        if num == 'Z':
            sum -= int(zArr[i-1])
        else:
            sum += int(num)

    return sum

# Solution
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer