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

# this solution uses del instead of pop
# need to understand why two arrays can be compared this way. Aren't they reference variables?
