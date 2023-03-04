import numpy as np
from math import inf


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
    moves = []
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                moves.append((i, j))
    return moves


def ab_prune(state, player):
    value, move = max_value(state, player, -inf, inf)
    return value, move


def max_value(state, player, alpha, beta):
    win_status = check_position(state, player)
    moves = actions(state)
    no_of_moves=len(moves)

    if win_status == 1 or win_status == -1 or moves == []:
        return win_status*no_of_moves, None

    v = -inf
    for a in actions(state):
        v2, a2 = min_value(play(state, player, a), player, alpha, beta)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_value(state, player, alpha, beta):
    win_status = check_position(state, player)
    moves = actions(state)
    no_of_moves=len(moves)

    if win_status == 1 or win_status == -1 or moves == []:
        return win_status*no_of_moves, None

    v = inf
    for a in actions(state):
        v2, a2 = max_value(play(state, -player, a), player, alpha, beta)
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
        print("Invalid")
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


def print_board(board):
    for i in range(n):
        print(f'    {i}', end="")
    print()
    for i in range(n):
        print(f'{i} ', end="")
        for j in range(n):
            print(f'| {a[board[i][j]]}', end=" |")
        print()


def play_with_computer():
    win = 0
    player = symbols[input("Choose x or o : ")]
    computer = -player
    moves_played = 0

    if player == 1:
        print_board(board)
        player_turn(player)
        moves_played += 1

    while moves_played < n*n:
        computer_turn(computer)
        moves_played += 1
        print_board(board)
        if check_position(board, computer):
            win = computer
            break

        if moves_played < n*n:
            player_turn(player)
            moves_played += 1
            print_board(board)
            if check_position(board, player):
                win = player
                break

    if win == player:
        print("Player wins")
    elif win == computer:
        print("Computer wins")
    elif win == 0:
        print("Draw")


def eval_position():
    
    print("Enter position\nx - Player\no - Opponent\n0 - Null")
    for i in range(n):
        for j in range(n):
            val = input()
            board[i][j] = symbols[val]
    player = input("Enter the current player (x or o) : ")

    value, move = ab_prune(board, symbols[player])
    print_board(board)
    print("Position status :", value)
    print("Best move       :", move)


n = 3
a = {1: 'X', -1: 'O', 0: ' '}
symbols = {'x': 1, 'o': -1, '0': 0}
board = np.zeros((n, n), dtype=int)
choice = int(input("1.Play with computer\n2.Evaluate a position\nChoice : "))

if choice == 1:
    play_with_computer()
if choice == 2:
    eval_position()
