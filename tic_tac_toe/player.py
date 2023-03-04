import numpy as np
n = 3

board = [[0]*n]*n
board = np.array(board)
print(board)


def play(player, i, j):
    if board[i][j] == 0:
        board[i][j] = player
        return True
    else:
        print("invalid")
        return False


def check_row(player):
    for i in range(n):
        status = True
        for j in range(n):
            if board[i][j] != player:
                status = False
                break
        if status:
            return True

    return False


def check_col(player):
    for i in range(n):
        status = True
        for j in range(n):
            if board[j][i] != player:
                status = False
                break
        if status:
            return True

    return False


def check_diag(player):
    status_left = True
    status_right = True
    for i in range(n):
        for j in range(n):
            if i == j and board[i][j] != player:
                status_left = False
            if i+j+1 == n and board[i][j] != player:
                status_right = False
    return status_left or status_right


def check_position(player):
    if check_row(player) or check_col(player) or check_diag(player):
        return True
    return False


player = 1
win = 0
moves = 0
while moves < n*n:
    i = int(input())
    j = int(input())
    if play(player, i, j):
        moves += 1
        print(board)
        if check_position(player):
            win = player
            break
        else:
            player *= -1
print(win)