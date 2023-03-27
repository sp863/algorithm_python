def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]

    count = 0

    for babble in babbling:
        temp = babble
        for word in words:
            temp = temp.replace(word, ' ')

        if len(temp.replace(' ', '')) == 0:
            count += 1

    return count

# Solution
def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c