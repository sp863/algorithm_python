def solution(numbers):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, word in enumerate(eng):
        numbers = numbers.replace(word, str(i))

    return int(numbers)

# Solution
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)