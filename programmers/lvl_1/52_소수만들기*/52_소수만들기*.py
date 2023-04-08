def isPrime(num):
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if isPrime(nums[i]+nums[j]+nums[k]):
                    count += 1
    return count

# Solution


def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1
    return answer

# need to learn how to use itertools.combinations for combination problems.
