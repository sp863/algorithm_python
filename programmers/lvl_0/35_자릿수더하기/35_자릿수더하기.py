def solution(n):
    return sum(int(num) for num in list(str(n)))

# Solution
def solution(n):
    answer = sum(list(map(int,list(str(n)))))
    return answer