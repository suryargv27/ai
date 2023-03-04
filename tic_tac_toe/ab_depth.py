import numpy as np
from math import inf
max_depth=3

def play(state, player, a):
    new_state = np.copy(state)
    new_state[a[0]][a[1]] = player
    return new_state


def check_pos(state, player):
    status_left_diag = True
    status_right_diag = True
    for i in range(n):
        status_row = True
        status_col = True

        for j in range(n):
            if state[i][j] != player:
                status_row = False
            if state[j][i] != player:
                status_col = False
            if i == j and state[i][j] != player:
                status_left_diag = False
            if i+j+1 == n and state[i][j] != player:
                status_right_diag = False

        if status_row:
            return True
        if status_col:
            return True
    return status_left_diag or status_right_diag


def check_position(state, player):
    if check_pos(state, player):
        return 1
    if check_pos(state, -player):
        return -1
    return 0


def actions(state):
    moves = []
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                moves.append((i, j))
    return moves


def ab_prune(state, player):
    value, move = max_value(state, player, -inf, inf,0)
    return value, move


def max_value(state, player, alpha, beta,depth):
    win_status = check_position(state, player)
    moves = actions(state)
    no_of_moves = len(moves)

    if win_status == 1 or win_status == -1 or moves == [] or depth>max_depth:
        return win_status * no_of_moves, None

    v = -inf
    for a in actions(state):
        v2, a2 = min_value(play(state, player, a), player, alpha, beta,depth+1)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_value(state, player, alpha, beta,depth):
    win_status = check_position(state, player)
    moves = actions(state)
    no_of_moves = len(moves)

    if win_status == 1 or win_status == -1 or moves == [] or depth>max_depth:
        return win_status * no_of_moves, None

    v = inf
    for a in actions(state):
        v2, a2 = max_value(play(state, -player, a), player, alpha, beta,depth+1)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move


def is_valid_move(player, i, j):
    if board[i][j] == 0:
        board[i][j] = player
        return True
    else:
        print("invalid")
        return False


def player_turn(player):
    played = False
    while not played:
        print("Enter Your Move")
        i = int(input())
        j = int(input())
        if is_valid_move(player, i, j):
            played = True


def computer_turn(computer):
    print("Computer Plays")
    value, move = ab_prune(board, computer)
    board[move[0]][move[1]] = computer


n = 4
board = np.zeros((n, n), dtype=int)
player = 1
win = 0

player = int(input("Choose First Player(1) or Second Player(-1) : "))
computer = -player
moves_played = 0

if player == 1:
    print(board)
    player_turn(player)
    moves_played += 1

while moves_played < n*n:
    computer_turn(computer)
    moves_played += 1
    print(board)
    if check_position(board, computer):
        win = computer
        break

    if moves_played < n*n:
        player_turn(player)
        moves_played += 1
        print(board)
        if check_position(board, player):
            win = player
            break

print(win)
