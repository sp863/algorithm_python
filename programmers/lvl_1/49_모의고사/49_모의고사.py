def get_score(answers, my_answers):
    score = 0
    for i in range(len(answers)):
        if answers[i] == my_answers[i]:
            score += 1
    return score


def solution(answers):
    first = [1, 2, 3, 4, 5] * 2500
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000

    first_score = get_score(answers, first)
    second_score = get_score(answers, second)
    third_score = get_score(answers, third)

    scores = [first_score, second_score, third_score]
    max_score = max(scores)

    return [i + 1 for i, my_score in enumerate(scores) if my_score == max_score]


# Solution

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# this solution is a lot clearer than mine.
# I like the use of enumerate and the use of the modulo operator to get the index of the pattern list.
