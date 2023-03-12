def solution(numbers, k):
    count = 0
    idx = 0

    while True:
        count += 1
        if count == k:
            break
        idx += 2
        if idx >= len(numbers):
            idx = idx - len(numbers)

    return numbers[idx]

# Solution
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1