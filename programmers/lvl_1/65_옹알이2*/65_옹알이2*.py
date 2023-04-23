def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya', 'ye', 'woo', 'ma']:
            if j*2 not in i:
                i = i.replace(j, ' ')
                print("i =", i)
        if len(i.strip()) == 0:
            answer += 1
    return answer

# Solution


def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya', 'ye', 'woo', 'ma']:
            if j*2 not in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            answer += 1
    return answer


def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count

# using j*2 to NOT count consecutive words
# using replace with empty space to consider cases where words may be combined after replacing with no space ''
