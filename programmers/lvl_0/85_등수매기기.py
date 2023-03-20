# Solution

def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

from functools import reduce
def solution(score):
    sorted_score = sorted(reduce(lambda x,y:x.append(sum(y)) or x,score,[]),reverse=True)

    return [sorted_score.index(sum(s))+1 for s in score]