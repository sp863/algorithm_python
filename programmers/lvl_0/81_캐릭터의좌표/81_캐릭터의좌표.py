def solution(keyinput, board):
    keyMap = {
        'left': -1,
        'right': 1,
        'up': 1,
        'down': -1
    }

    x_max = (board[0] - 1) // 2
    y_max = (board[1] - 1) // 2
    x_min = -x_max
    y_min = -y_max

    answer = [0, 0]

    for dir in keyinput:
        if dir == 'left' or dir == 'right':
            answer[0] += keyMap[dir]
            if answer[0] < x_min or answer[0] > x_max:
                if answer[0] > 0:
                    answer[0] = x_max
                else:
                    answer[0] = x_min
        else:
            answer[1] += keyMap[dir]
            if answer[1] < y_min or answer[1] > y_max:
                if answer[1] > 0:
                    answer[1] = y_max
                else:
                    answer[1] = y_min

    return answer

# Solution
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]