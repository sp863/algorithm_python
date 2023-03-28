def solution(array, n):
    diffArray = [abs(n - num) for num in sorted(array)]
    idx = diffArray.index(min(diffArray))
    return sorted(array)[idx]

# Solution
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer