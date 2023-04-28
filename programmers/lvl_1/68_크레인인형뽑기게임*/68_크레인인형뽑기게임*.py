def solution(board, moves):
    bucket = []
    answer = 0

    for move in moves:
        for y in range(len(board)):
            if board[y][move-1] != 0:
                bucket.append(board[y][move-1])
                board[y][move-1] = 0

                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer += 2
                break

    return answer

# Solution


def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer

# Need to solve this problem again.
