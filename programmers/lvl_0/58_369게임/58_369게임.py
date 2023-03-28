def solution(order):
    clap = 0
    for num in str(order):
        if int(num) == 3 or int(num) == 6 or int(num) == 9:
            clap += 1
    return clap

# Solution
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer