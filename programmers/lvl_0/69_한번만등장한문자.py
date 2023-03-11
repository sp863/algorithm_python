def solution(s):
    return ''.join(letter for letter in sorted(list(set(s))) if s.count(letter) == 1)