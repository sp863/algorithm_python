def solution(my_string):
    arr = my_string.split()

    sum = int(arr[0])
    for x in range(1, len(arr)):
        if arr[x] == '+':
            sum += int(arr[x+1])
        elif arr[x] == '-':
            sum -= int(arr[x+1])

    return sum

# Solution
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))