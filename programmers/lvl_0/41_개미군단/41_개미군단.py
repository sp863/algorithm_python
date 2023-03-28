def solution(hp):
    star, remain = divmod(hp, 5)
    cap, remain2 = divmod(remain, 3)
    sol = remain2 // 1

    return star + cap + sol

# Solution
def solution(hp):
    answer = 0
    answer += hp//5
    hp %= 5
    answer += hp//3
    hp %= 3
    answer += hp//1

    return answer