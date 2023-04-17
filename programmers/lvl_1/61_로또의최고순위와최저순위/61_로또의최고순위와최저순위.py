def solution(lottos, win_nums):
    prize = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6,
    }

    count = 0
    count_zeros = lottos.count(0)

    for lotto in lottos:
        if lotto in win_nums:
            count += 1

    max = prize[count + count_zeros]
    min = prize[count]

    return [max, min]

# Solution


def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]

# why didn't I think of using rank as an array?...
