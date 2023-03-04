from math import inf


def generate_win_numbers(n):
    win_numbers = []
    left_diag = []
    right_diag = []
    for i in range(n):
        row = []
        col = []
        for j in range(n):
            row.append(i*n+j)
            col.append(j*n+i)
        win_numbers.append(row)
        win_numbers.append(col)
        left_diag.append(i*(n+1))
        right_diag.append((i+1)*(n-1))
    win_numbers.append(left_diag)
    win_numbers.append(right_diag)

    return win_numbers


def number_to_bin(state):
    bin_state = 0
    for val in state:
        bin_state = bin_state | (1 << (n*n-1-val))
    return bin_state


def generate_win_comb(n):
    win_numbers = generate_win_numbers(n)
    win_comb = []
    for number in win_numbers:
        win_comb.append(number_to_bin(number))
    return win_comb


def check_position(state):
    for win in win_comb:
        if state & win == win:
            return 1
    return 0


def ab_prune(player_state, opponent_state):
    available_moves = [i for i in range(n*n)]
    value, move = max_value(
        player_state, opponent_state, -inf, inf, available_moves)
    return value, move


def max_value(player_state, opponent_state, alpha, beta, available_moves):
    opponent_win_status = check_position(opponent_state)

    if opponent_win_status == 1 or available_moves == []:
        return -opponent_win_status, None

    v = -inf
    for a in available_moves:
        new_moves = available_moves[1:]
        v2, a2 = min_value(player_state | (1 << (n*n-1-a)),
                           opponent_state, alpha, beta, new_moves)
        if v2 > v:
            v, move = v2, a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_value(player_state, opponent_state, alpha, beta, available_moves):
    player_win_status = check_position(player_state)

    if player_win_status == 1 or available_moves == []:
        return 1*player_win_status, None

    v = inf
    for a in available_moves:
        new_moves = available_moves[1:]
        v2, a2 = max_value(player_state, opponent_state | (
            1 << (n*n-1-a)), alpha, beta, new_moves)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move


n = 4
win_comb = generate_win_comb(n)

print(ab_prune(0b0, 0b0))