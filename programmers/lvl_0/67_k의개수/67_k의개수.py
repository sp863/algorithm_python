def solution(i, j, k):
    count = 0
    for num in range (i, j + 1):
        count += str(num).count(str(k))
    return count

# Solution
def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer

def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))