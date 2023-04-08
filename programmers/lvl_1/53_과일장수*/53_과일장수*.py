def solution(k, m, score):
    sorted_score = sorted(score)
    apples = sorted_score[len(sorted_score) % m:]

    answer = 0
    for i in range(0, len(apples), m):
        temp_apples = [apples[j] for j in range(i, i + m)]
        answer += min(temp_apples) * m

    return answer


# Solution

def solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m])*m

# this solution is a lot simpler than mine....
