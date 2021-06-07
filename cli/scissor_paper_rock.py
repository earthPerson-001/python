from random import *
outcome = " "
b = " "


def random_number_generator():
    r = randint(0, 3)
    outcomes = ["scissor", "paper", "rock"]
    global outcome
    outcome = outcomes[r]


def input_acceptor():
    a = input("Enter your guess: ('rock', 'paper' or 'scissor)")
    global b
    b = a.lower()


def game(result, a):
    if result == a:
        print("The computer's entered  {0} and you've entered {1} so the game ended in tie".format(result, a))
    elif result == "scissor" and a == "rock" or result == "paper" and a == "scissor" or result == "rock" and a == "paper":
        print("The computer's entered {0} and you've entered {1} so you've won the game".format(result, a))
    else:
        print("The computer's entered {0} and you've entered {1} so you've lost the game".format(result, a))


random_number_generator()
input_acceptor()
game(outcome, b)






