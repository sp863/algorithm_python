def solution(n):
    min, ext = divmod(n, 7)

    return min + int(ext != 0)

# Solution
def solution(n):
    return (n - 1) // 7 + 1