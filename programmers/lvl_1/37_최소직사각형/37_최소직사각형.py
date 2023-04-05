def solution(sizes):
    x = []
    y = []

    for size in sizes:
        x.append(max(size))
        y.append(min(size))

    return max(x) * max(y)

# Solution


def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
