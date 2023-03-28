def solution(emergency):
    sortedEmerg = sorted(emergency, reverse = True)
    return [sortedEmerg.index(num) + 1 for num in emergency]

# Solution
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]