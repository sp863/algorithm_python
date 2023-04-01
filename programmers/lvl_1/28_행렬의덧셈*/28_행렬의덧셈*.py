def solution(arr1, arr2):
    combined = [list(zip(arr1[i], arr2[i])) for i in range(len(arr1))]
    answer = []
    for num in combined:
        answer.append([tup[0]+tup[1] for tup in num])

    return answer

# Solution


def solution(A, B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]


def solution(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer
