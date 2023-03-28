def solution(num, k):
    for i, num in enumerate(str(num)):
        if num == str(k):
            return i + 1
    return -1

# Solution
def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1