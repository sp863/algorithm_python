def solution(slice, n):
    if slice >= n:
        return 1

    minimum = n // slice

    if n % slice > 0:
        minimum += 1

    return minimum

# Solution
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)

def solution(slice, n):
    return (n + slice - 1) // slice