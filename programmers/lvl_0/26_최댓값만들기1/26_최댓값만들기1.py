def solution(numbers):
    sortedArr = sorted(numbers)
    return sortedArr[-1] * sortedArr[-2]

# Solution
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]