def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        count = 0
        for n in range(1, num+1):
            if num % n == 0:
                count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

# Solution


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer

# int(i**0.5) == i**0.5 -> square root of i, if it is an integer, then it is a perfect square
# if it is a perfect square, then it has an odd number of divisors
# if it is not a perfect square, then it has an even number of divisors
