def solution(price, money, count):
    cost = money - sum([c*price for c in range(1, count+1)])
    return abs(cost) if cost < 0 else 0

# Solution


def solution(price, money, count):
    return max(0, price*(count+1)*count//2-money)

# Arithmetic sequence used...need formula
