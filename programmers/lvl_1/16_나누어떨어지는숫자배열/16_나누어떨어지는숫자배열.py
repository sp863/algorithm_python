def solution(arr, divisor):
    answer_arr = sorted([num for num in arr if num % divisor == 0])
    return answer_arr if len(answer_arr) > 0 else [-1]

# Solution


def solution(arr, divisor): return sorted(
    [n for n in arr if n % divisor == 0]) or [-1]
