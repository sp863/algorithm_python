def solution(numbers, direction):
    answer = [0] * len(numbers)
    if direction == 'right':
        for idx, num in enumerate(numbers):
            if idx == len(numbers) - 1:
                answer[0] = num
            else:
                answer[idx + 1] = num

    else:
        for idx, num in enumerate(numbers):
            if idx == 0:
                answer[len(numbers) - 1] = num
            else:
                answer[idx - 1] = num


    return answer

# Solution
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

def solution(numbers, direction):
    if direction == "right":
        answer = [numbers[-1]] + numbers[:len(numbers)-1]
    else:
        answer = numbers[1:] + [numbers[0]]
    return answer