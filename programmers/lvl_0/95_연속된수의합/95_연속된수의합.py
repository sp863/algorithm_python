def solution(num, total):
    d = 0
    for i in range(1, num):
        d += i
    start= (total - d) // num
    return [i for i in range(start, start + num)]

# Solution
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]

def solution(num, total):
    answer = []
    var = sum(range(num + 1))
    diff = total - var
    start_num = diff // num
    answer = [i + 1 + start_num for i in range(num)]
    return answer
