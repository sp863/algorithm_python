def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)

# Solution
def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )