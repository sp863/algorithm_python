def solution(before, after):
    count = 0

    for letter in before:
        if before.count(letter) == after.count(letter):
            count += 1

    return 1 if count == len(before) else 0

# Solution
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0