def solution(N, stages):
    players = len(stages)
    prob_dict = {}

    for i in range(1, N+1):
        if players != 0:
            prob_dict[i] = stages.count(i) / players
            players -= stages.count(i)
        else:
            prob_dict[i] = 0

    return sorted(prob_dict, key=lambda x: prob_dict[x], reverse=True)

# Solution


def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

# Need to understand why the conditional statement is necessary...why zero
