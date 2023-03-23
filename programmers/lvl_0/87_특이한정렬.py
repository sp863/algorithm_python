def solution(numlist, n):
    diff_array = list(map(lambda x: (x, abs(n - x)), sorted(numlist, reverse=True)))
    sorted_diff = sorted(diff_array, key=lambda x: x[1])

    return list(map(lambda x: x[0], sorted_diff))

# Solution
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

def solution(numlist, n):
    return sorted(numlist,key = lambda x: [abs(x-n),-x])
