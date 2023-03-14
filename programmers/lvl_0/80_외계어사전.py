def solution(spell, dic):
    count = 0
    for word in dic:
        include_sum = len([letter for letter in spell if word.count(letter) == 1])
        if len(spell) == include_sum:
            count += 1

    return 1 if count > 0 else 2

# Solution
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
