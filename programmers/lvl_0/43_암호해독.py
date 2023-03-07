def solution(cipher, code):
    return ''.join([letter for idx, letter in enumerate(cipher) if (idx + 1) % code == 0])

# Solution
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer