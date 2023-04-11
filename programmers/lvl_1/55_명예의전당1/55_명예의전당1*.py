def solution(k, scores):
    answer = []
    top = []

    for score in scores:
        top.append(score)
        top = sorted(top, reverse=True)[:k]

        answer.append(min(top))

    return answer

# Solution


def solution(k, score):
    q = []
    answer = []

    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer

# incorrect on the first try
