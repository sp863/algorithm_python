def solution(lines):
    start = [line[0] for line in lines]
    end = [line[1] for line in lines]

    overlapped = 0

    for point in range(min(start), max(end) + 1):
        count = 0
        for i in range(len(lines)):
            if point >= start[i] and point < end[i]:
                count += 1

        if count >= 2:
            overlapped += 1

        count = 0

    return overlapped

# Solution
def solution1(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

def solution(lines):
    line = [0] * 200

    for a, b in lines:
        for i in range(a, b):
            line[i + 100] += 1

    return sum(1 for count in line if count > 1)