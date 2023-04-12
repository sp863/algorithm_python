def solution(name, yearning, photo):
    map = {}

    for i in range(len(name)):
        map[name[i]] = yearning[i]

    return [sum([map[name] if name in map else 0 for name in p]) for p in photo]

# Solution


def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    scores = []
    for pt in photo:
        score = 0
        for p in pt:
            if p in dictionary:
                score += dictionary[p]
        scores.append(score)
    return scores
