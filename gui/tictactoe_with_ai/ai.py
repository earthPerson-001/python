import random

n = 0
outcomes = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]


def state_checker(input_1, input_2, depth, current_list):
    for i in outcomes:
        def tie_checker():
            tie_counter = 0
            for j in current_list:
                if not j == 0:
                    tie_counter += 1
            if tie_counter > 8:
                return True
            return False
        player1 = len(set(i).intersection(set(input_1))) > 2
        player2 = len(set(i).intersection(set(input_2))) > 2
        tie = False
        if not player1 and not player2:
            tie = tie_checker()

        while player1 or player2 or tie:
            score1 = 0
            if player1:
                score1 = -10 - depth
            elif player2:
                score1 = 10 + depth
            elif tie:
                score1 = 0
            return score1
    return False


def best_position_selector(current_board, input_1, input_2, t):
    alpha = -1000
    beta = 1000
    best_position = 0
    best_score = -10000000000
    if len(input_1) + len(input_2) < 2:
        return random.choices([0, 2, 4, 6, 8])[0]
    else:
        for k in range(9):
            if current_board[k] == 0:
                current_board[k] = t
                input_2.append(k)
                core = minimax(current_board, False, 9, input_1, input_2, alpha, beta, t)
                if core > best_score:
                    best_score = core
                    best_position = k
                current_board[k] = 0
                del input_2[input_2.index(k)]
                if alpha >= beta:
                    return best_position
        return best_position


def minimax(current_board, maximizing, depth, input_1, input_2, alpha, beta, t):
    global n
    n += 1
    if state_checker(input_1, input_2, depth, current_board) is False:
        if maximizing:
            best_score = -10000000000
            for d in range(9):
                if current_board[d] == 0:
                    current_board[d] = t
                    input_2.append(d)
                    core = minimax(current_board, False, depth - 1, input_1, input_2, alpha, beta, t)
                    current_board[d] = 0
                    del input_2[input_2.index(d)]
                    if alpha >= beta:
                        return best_score
            return best_score
        else:
            best_score = 10000000000
            for c in range(9):
                if current_board[c] == 0:
                    current_board[c] = t
                    input_1.append(c)
                    core = minimax(current_board, True, depth - 1, input_1, input_2, alpha, beta, t)
                    best_score = min(best_score, core)
                    current_board[c] = 0
                    del input_1[input_1.index(c)]
                    if beta <= alpha:
                        return best_score
            return best_score
    else:
        return state_checker(input_1, input_2, depth, current_board)


def game_checker(current_list, input_1, input_2):
    player1, player2, tie = False, False, False
    for i in outcomes:
        def tie_checker():
            tie_counter = 0
            for j in current_list:
                if not j == 0:
                    tie_counter += 1
            if tie_counter > 8:
                return True
            return False
        player1 = len(set(i).intersection(set(input_1))) > 2
        player2 = len(set(i).intersection(set(input_2))) > 2
        tie = False
        if not player1 and not player2:
            tie = tie_checker()

    if player1 or player2 or tie:
        return True
