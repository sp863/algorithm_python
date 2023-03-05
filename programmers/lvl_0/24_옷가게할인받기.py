def solution(price):
    factor = 100000

    if price >= factor * 5:
        return int(price * 0.8)
    if price >= factor * 3:
        return int(price * 0.9)
    if price >= factor:
        return int(price * 0.95)

    return price

# Solution
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)