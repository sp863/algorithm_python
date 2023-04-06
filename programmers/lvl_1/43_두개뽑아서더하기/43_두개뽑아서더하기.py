def solution(numbers):
    temp = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp.add(numbers[i] + numbers[j])

    return sorted(list(temp))

# Solution


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

# you can use set to remove duplicates just by casting array to a set
