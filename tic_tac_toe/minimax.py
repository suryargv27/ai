import numpy as np
import copy
from math import inf
n = 3


def play(state, player, a):
    new_state = np.copy(state)
    new_state[a[0]][a[1]] = player
    return new_state


def check_row(state, player):
    for i in range(n):
        status = True
        for j in range(n):
            if state[i][j] != player:
                status = False
                break
        if status:
            return True

    return False


def check_col(state, player):
    for i in range(n):
        status = True
        for j in range(n):
            if state[j][i] != player:
                status = False
                break
        if status:
            return True

    return False


def check_diag(state, player):
    status_left = True
    status_right = True
    for i in range(n):
        for j in range(n):
            if i == j and state[i][j] != player:
                status_left = False
            if i+j+1 == n and state[i][j] != player:
                status_right = False
    return status_left or status_right


def check_position(state, player):
    if check_row(state, player) or check_col(state, player) or check_diag(state, player):
        return 1
    if check_row(state, -player) or check_col(state, -player) or check_diag(state, -player):
        return -1
    return 0


def actions(state):
    available_moves = []
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                available_moves.append((i, j))
    return available_moves


def minimax(state, player):
    value, move = max_value(state, player)
    return value, move


def max_value(state, player):
    win_status = check_position(state, player)

    if win_status == 1 or win_status == -1:
        return win_status, None

    if actions(state) == []:
        return win_status, None

    v = -inf
    for a in actions(state):
        v2, a2 = min_value(play(state, player, a), player)
        if v2 > v:
            v, move = v2, a
    return v, move


def min_value(state, player):
    win_status = check_position(state, player)

    if win_status == 1 or win_status == -1:
        return win_status, None

    if actions(state) == []:
        return win_status, None

    v = inf
    for a in actions(state):
        v2, a2 = max_value(play(state, -player, a), player)
        if v2 < v:
            v, move = v2, a
    return v, move


start = [[1, -1, 0],
         [1, 0, 0],
         [-1, 0, 0]]
start = np.array(start)
player = 1
print(minimax(start, player))
