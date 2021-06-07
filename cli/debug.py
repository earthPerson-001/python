# Global variables
from itertools import permutations

under_score = " ____________"
board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
turn = "X"
index = " "
player_1_inputlist = []
player_2_inputlist = []


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


def game_logic():
    permutation = [permutations([1, 2, 3]), permutations([4, 5, 6]), permutations([7, 8, 9]), permutations([1, 4, 7]),
                   permutations([2, 5, 8]), permutations([3, 6, 9]), permutations([1, 5, 9]), permutations([3, 5, 7])]
    for i in permutation:
        for j in list(i):
            if all(elem in player_1_inputlist for elem in j):
                print("Player 1 has won the game")
                return True
            elif all(elem in player_2_inputlist for elem in j):
                print("Player 2 has won the game")
                return True
            elif len(player_1_inputlist) + len(player_2_inputlist) > 8:
                print("The game has ended in tie")
                return True


def game():  # game
    global player_1_inputlist, player_2_inputlist
    while not game_logic():
        game_board()
        try:
            print(turn + "'s turn")
            p = (int(input("Where do you want to mark : {0}?".format(
                list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(set(player_1_inputlist).union(player_2_inputlist)))))) - 1)
            while p not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print("Please select integers between 1-9")
                p = (int(input("Where do you want to mark : {0}?".format(
                    list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(set(player_1_inputlist).union(player_2_inputlist)))))) - 1)
            while board[p] != "   ":
                print("The place index you've entered has already been filled, please enter another one.")
                p = (int(input("Where do you want to mark : {0}?".format(
                    list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(set(player_1_inputlist).union(player_2_inputlist)))))) - 1)
            if turn == "X":
                player_1_inputlist.append(p + 1)
            elif turn == "O":
                player_2_inputlist.append(p + 1)
            board[p] = " {0} ".format(turn)
            turn_selector()
        except ValueError:
            print("Please enter integers between (1 - 9)")


game()  # calls the game
game_board()  # Displays the game result
