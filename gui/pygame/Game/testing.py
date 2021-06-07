def best_position_selector(self, current_board, isai, input_1, input_2):
    depth = 0
    mainboard = current_board
    maininputs = [input_1, input_2]
    best_position = random.choices(list(set(range(0, 9)) - set(input_1) - set(input_2)))[0]
    while depth < 1:
        best_score = 0
        c = 0
        for position in current_board:
            if isai:
                if position == " ":
                    input_2.append(c)
                    core = self.score_counter(input_1, input_2)
                    if core > best_score:
                        best_position = c
                    current_board[best_position] = 'O'
                    best_score = best_score + core
                    isai = False
            if not isai:
                if position == " ":
                    current_board[c] = 'X'
                    input_1.append(c)
                    core = self.score_counter(input_1, input_2)
                    if core < best_score:
                        best_position = c
                    current_board[best_position] = 'X'
                    best_score = best_score + core
                    isai = True
        input_1 = maininputs[0]
        input_2 = maininputs[1]
        current_board = mainboard

        c += 1
    depth += 1

    return best_position
