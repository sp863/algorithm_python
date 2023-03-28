def solution(n):
    return int(''.join(map(str, sorted(list(map(int, str(n))), reverse=True))))

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))