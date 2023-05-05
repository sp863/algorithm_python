def solution(ingredient):
    stack = []
    count = 0

    for ing in ingredient:
        stack.append(ing)
        if stack[-4:] == [1, 2, 3, 1]:
            count += 1
            for _ in range(4):
                stack.pop()

    return count

# Solution


def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del s[-4:]
    return cnt


def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            s = s[:-4]  # 해당 부분으로 인해 시간 초과 발생
    return cnt

# this solution uses del instead of pop
# need to understand why two arrays can be compared this way. Aren't they reference variables?
# last solution is incorrect and can cause runtime error. why?
# del s[-4:] is faster than s = s[:-4] because the latter creates a new array and assigns it to s
