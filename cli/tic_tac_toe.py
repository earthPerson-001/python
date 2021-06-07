# Global variables
under_score = " ____________"
board = ["   ", "   ", "   ",
         "   ", "   ", "   ",
         "   ", "   ", "   "]
turn = "X"
index = " "
input_list = []


def game_board():  # Draws game board
    print(under_score)
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print(under_score)
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print(under_score)
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print(under_score)


def turn_selector():  # Determines whose turn is it.
    global turn
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"


def row_win():  # Determines if any row has all same elements.
    global index
    if board[0] == board[1] == board[2] != "   ":
        index = board[0]
        return True
    elif board[3] == board[4] == board[5] != "   ":
        index = board[3]
        return True
    elif board[6] == board[7] == board[8] != "   ":
        index = board[6]
        return True
    else:
        return False


def column_win():  # determines if any column has all same elements.
    global index
    if board[0] == board[3] == board[6] != "   ":
        index = board[0]
        return True
    elif board[1] == board[4] == board[7] != "   ":
        index = board[1]
        return True
    elif board[2] == board[5] == board[8] != "   ":
        index = board[2]
        return True
    else:
        return False


def diagonal_win():  # Determines if any diagonal has all same elements.
    global index
    if board[0] == board[4] == board[8] != "   ":
        index = board[0]
        return True
    elif board[2] == board[4] == board[6] != "   ":
        index = board[2]
        return True
    else:
        return False


def game_won():  # Determines if any player has won the game.
    if row_win() or column_win() or diagonal_win():
        print(index, "has won the game")
        return True
    else:
        return False


def game_tie():  # Determines if the game has tied.(Tweaking needed)
    if board[0] != "   " and board[1] != "   " and board[2] != "   " and board[3] != "   " and board[4] != "   " and board[5] != "   " and board[6] != "   " and board[7] != "   " and board[8] != "   ":
        return True


def game():  # game
    global input_list
    while not game_won() and not game_tie():
        game_board()
        try:
            print(turn + "'s turn")
            p = (int(input("Where do you want to mark : {0}?".format(list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(input_list))))) - 1)
            while p not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print("Please select integers between 1-9")
                p = (int(input("Where do you want to mark : {0}?".format(
                    list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(input_list))))) - 1)
            while board[p] != "   ":
                print("The place index you've entered has already been filled, please enter another one.")
                p = (int(input("Where do you want to mark : {0}?".format(
                        list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(input_list))))) - 1)

            input_list.append(p + 1)
            board[p] = " {0} ".format(turn)
            turn_selector()
        except ValueError:
            print("Please enter integers between (1 - 9)")


game()  # calls the game
game_board()  # Displays the game result
