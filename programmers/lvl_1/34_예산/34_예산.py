def solution(d, budget):
    sorted_money = sorted(d)
    count = 0

    for money in sorted_money:
        if budget - money >= 0:
            count += 1
            budget -= money
        else:
            break

    return count

# Solution


def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
