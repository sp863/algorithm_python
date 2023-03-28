def solution(n):
    for num in range(2, n):
        if n % num == 1:
            return num

# Solution
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]

def solution(n):
    return next(i for i in range(2, n) if n % i == 1)