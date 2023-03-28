def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(i for i in my_string if i not in vowels)

# Solution
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])