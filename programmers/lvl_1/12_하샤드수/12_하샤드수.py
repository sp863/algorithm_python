def solution(x):
    return True if x % sum(map(int, str(x))) == 0 else False

# Solution
def Harshad(n):
    return n % sum(int(x) for x in str(n)) == 0