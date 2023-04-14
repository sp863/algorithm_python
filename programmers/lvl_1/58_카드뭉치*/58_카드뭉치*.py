def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx1, idx2 = 0, 0

    for word in goal:
        if len(cards1) > idx1 and word == cards1[idx1]:
            idx1 += 1
        elif len(cards2) > idx2 and word == cards2[idx2]:
            idx2 += 1
        else:
            answer = "No"
            break

    return answer

# Solution


def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
