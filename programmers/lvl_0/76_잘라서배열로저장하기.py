def solution(my_str, n):
    answer = []

    count = 0
    idx = 0
    for i, x in enumerate(my_str):
        count += 1
        if count % n == 0:
            answer.append(my_str[idx:i+1])
            idx = i + 1
            count = 0
            continue

        if i == len(my_str) - 1:
            answer.append(my_str[idx:len(my_str)])

    return answer

# Solution
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]