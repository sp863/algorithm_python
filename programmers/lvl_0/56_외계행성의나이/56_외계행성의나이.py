def solution(age):
    alpha = "abcdefghij"
    ageNum = list(str(age))
    return ''.join([alpha[int(num)] for num in ageNum])