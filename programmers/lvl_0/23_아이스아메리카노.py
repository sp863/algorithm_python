def solution(money):
    cups, change = divmod(money, 5500)
    return [cups, change]

 # Solution
def solution(money):
    return [money // 5500, money % 5500]

def solution(money):
    return divmod(money, 5500)