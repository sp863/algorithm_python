def solution(num):
    if num == 1:
        return 0
    
    count = 0
    temp = num
    
    while temp > 1:
        if count >= 500:
            return -1
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = temp * 3 + 1
        
        count += 1
    
    return count

# Solution
def solution(num):
    if num == 1: return 0

    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i + 1
    return -1