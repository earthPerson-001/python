from tkinter import *
from random import *
outcome = " "
a = " "
com = 0
user = 0
tie = 0
root = Tk()


def random_number_generator():
    r = randint(0, 2)
    outcomes = ["scissor", "paper", "rock"]
    global outcome
    outcome = outcomes[r]


def scissor():
    global a
    a = "scissor"


def paper():
    global a
    a = "paper"


def rock():
    global a
    a = "rock"


def game(result, c):
    global com, user, tie
    if result == c:
        tie += 1
        label_1 = Label(frame_2, text="The computer's entered  {0} and you've entered {1}"
                                      " so the game ended in tie".format(result, c))
    elif result == "scissor" and c == "rock" or result == "paper" and c == "scissor"\
            or result == "rock" and c == "paper":
        user += 1
        label_1 = Label(frame_2, text="The computer's entered {0} and you've entered {1}"
                                      " so you've won the game".format(result, c))
    else:
        label_1 = Label(frame_2, text="The computer's entered {0} and you've entered {1}"
                                      " so you've lost the game".format(result, c))
        com += 1
    label_1.grid(row=0, column=0, sticky=E+W)
    label_2 = Label(frame_3, text="Your score: {0}\ncomputer's score: {1}\ntie: {2}".format(user, com, tie))
    label_2.grid(row=0, column=0, sticky=E+W)


def game_starter():
    random_number_generator()
    game(outcome, a)


frame_1 = LabelFrame(root, padx=100, pady=50, bg="grey")
frame_2 = LabelFrame(root, padx=100, pady=50, bg="#225566")
frame_3 = LabelFrame(root, padx=50, pady=100, bg="green")

button_1 = Button(frame_1, text="scissor", command=scissor, bg="red", fg="white", padx=40, pady=30)
button_2 = Button(frame_1, text="paper", command=paper, bg="blue", fg="white", padx=40, pady=30)
button_3 = Button(frame_1, text="rock", command=rock, bg="magenta", fg="white", padx=40, pady=30)
button_4 = Button(frame_1, text="enter", command=game_starter, padx=40, pady=30)


frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1, sticky=N+S)
frame_3.grid(row=1, column=0, columnspan=2, sticky=W+E)

button_1.grid(row=0, column=0, padx=20, pady=10)
button_2.grid(row=1, column=0, padx=20, pady=10)
button_3.grid(row=2, column=0, padx=20, pady=10)
button_4.grid(row=3, column=0, padx=20, pady=10)


root.mainloop()
