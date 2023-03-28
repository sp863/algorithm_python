def solution(numbers):
    sortedNums = sorted(numbers)
    lastTwo = sortedNums[-1] * sortedNums[-2]
    firstTwo = sortedNums[0] * sortedNums[1]

    return firstTwo if firstTwo > lastTwo else lastTwo

# Solution
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 