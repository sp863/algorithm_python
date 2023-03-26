import copy

def solution(board):
    explode_region = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    answer_board = copy.deepcopy(board)
    check_board = [[False] * len(board[0])] * len(board)

    for i, row in enumerate(answer_board):
        for j, col in enumerate(row):
            if board[i][j] == 1 or (col == 1 and check_board[i][j] == False):
                check_board[i][j] = True
                for region in explode_region:
                    dy = i + region[0]
                    dx = j + region[1]
                    if dx >= len(answer_board[i]):
                        dx = len(answer_board[i]) - 1
                    if dx < 0:
                        dx = 0
                    if dy >= len(answer_board):
                        dy = len(answer_board) - 1
                    if dy < 0:
                        dy = 0

                    answer_board[dy][dx] = 1
                    check_board[dy][dx] = True

    count = 0
    for row in answer_board:
        for col in row:
            if col == 0:
                count += 1

    return count

# Solution
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer
