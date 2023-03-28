def solution(num_list, n):
    answer = []
    tempArr = []
    for num in num_list:
        tempArr.append(num)
        if (len(tempArr) == n):
            answer.append(tempArr)
            tempArr = []

    return answer

# Solution
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer