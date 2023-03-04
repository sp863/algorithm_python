def solution(array, height):
    tallerCount = 0

    for stu in array:
        if stu > height:
            tallerCount += 1;

    return tallerCount

# Solution
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

def solution(array, height):
    return sum(1 for a in array if a > height)