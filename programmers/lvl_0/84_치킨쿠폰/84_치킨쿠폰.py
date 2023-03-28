def solution(chicken):
    ordered = 0
    coupons = chicken

    while coupons >= 10:
        ordered += (coupons // 10)
        coupons = (coupons // 10) + (coupons % 10)

    return ordered

# Solution
def solution(chicken):
    return int(chicken*0.11111111111)

def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer