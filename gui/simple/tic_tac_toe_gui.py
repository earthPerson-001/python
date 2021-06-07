from tkinter import *
from tkinter import messagebox
import ai

if __name__ == "__main__":
    t = "O"

    root = Tk()
    root.title("Tic Tac Toe(main)")

    player_1 = False
    player_2 = False
    tie = False

    def start_game():
        list_buttons = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        outcomes = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
        player_1_inputs = []
        player_2_inputs = []
        top_level = Toplevel(root)
        top_level.title("Tic Tic Toe(game)")

        def first_turn():
            for i in list_buttons:
                if i != " ":
                    return False

            return True

        def game_board():
            b1 = Button(top_level, text=list_buttons[0], font="times 15",
                        bg="#81d4fa", fg="#000000", width=20, height=10, command=lambda: button(0))
            b2 = Button(top_level, text=list_buttons[1], font="times 15",
                        bg="#81d4fa", fg="#000000", width=20, height=10, command=lambda: button(1))
            b3 = Button(top_level, text=list_buttons[2], font="times 15",
                        bg="#81d4fa", fg="#000000", width=20, height=10, command=lambda: button(2))
            b4 = Button(top_level, text=list_buttons[3], font="times 15",
                        bg="#039be5", fg="#000000", width=20, height=10, command=lambda: button(3))
            b5 = Button(top_level, text=list_buttons[4], font="times 15",
                        bg="#039be5", fg="#000000", width=20, height=10, command=lambda: button(4))
            b6 = Button(top_level, text=list_buttons[5], font="times 15",
                        bg="#039be5", fg="#000000", width=20, height=10, command=lambda: button(5))
            b7 = Button(top_level, text=list_buttons[6], font="times 15",
                        bg="#01579b", fg="#000000", width=20, height=10, command=lambda: button(6))
            b8 = Button(top_level, text=list_buttons[7], font="times 15",
                        bg="#01579b", fg="#000000", width=20, height=10, command=lambda: button(7))
            b9 = Button(top_level, text=list_buttons[8], font="times 15",
                        bg="#01579b", fg="#000000", width=20, height=10, command=lambda: button(8))

            b1.grid(row=0, column=0)
            b2.grid(row=0, column=1)
            b3.grid(row=0, column=2)
            b4.grid(row=1, column=0)
            b5.grid(row=1, column=1)
            b6.grid(row=1, column=2)
            b7.grid(row=2, column=0)
            b8.grid(row=2, column=1)
            b9.grid(row=2, column=2)

        def button(a):
            while a not in player_1_inputs and a not in player_2_inputs:
                if t == "X":
                    player_1_inputs.append(a)
                    list_buttons[a] = t
                    game()
                    turn_selector()
                    bt1 = int(ai.best_position_selector(list_buttons, player_1_inputs, player_2_inputs, "O"))
                    button_b(bt1)

        def button_b(b):
            while b not in player_1_inputs and b not in player_2_inputs:
                if t == "O":
                    player_2_inputs.append(b)
                    list_buttons[b] = "O"
                    game()
                    turn_selector()

        def turn_selector():
            global t
            if t == "X":
                t = "O"
            elif t == "O":
                if t == 'O':
                    t = "X"

        def game():
            game_board()

            def winner_checker():
                for i in outcomes:
                    global player_1, player_2, tie
                    player1 = len(set(i).intersection(set(player_1_inputs))) > 2
                    player2 = len(set(i).intersection(set(player_2_inputs))) > 2

                    def tie_checker():
                        tie_counter = 0
                        for j in list_buttons:
                            if not j == " ":
                                tie_counter += 1
                        if tie_counter > 8:
                            return True
                        return False

                    tie = False
                    if not player1 and not player2:
                        tie = tie_checker()

                    if player1 or player2 or tie:
                        if player1:
                            messagebox.showinfo("Game results", "Player 1 has won the game")
                        elif player2:
                            messagebox.showinfo("Game results", "Computer has won the game")
                        elif tie:
                            messagebox.showinfo("Game results", "The game has ended in tie")
                        contd = messagebox.askyesno("Continue game", "Do you want to continue ?")
                        if contd:
                            root.forget(top_level)
                        elif not contd:
                            root.quit()
                        break
            winner_checker()
        if first_turn():
            bt = int(ai.best_position_selector(list_buttons, player_1_inputs, player_2_inputs, "O"))
            button_b(bt)
        game()


    frame_1 = LabelFrame(root, padx=100, pady=60, bg="#222299")
    frame_2 = LabelFrame(root, padx=100, pady=100, bg="#995522")

    label = Label(frame_1, text="Welcome to Tic Tac Toe by\n Bishal Neupane",
                  font="calibre 15", bg='#1245a8', fg='#999911', anchor="center")
    button_1 = Button(frame_2, text="Start Game", anchor=CENTER, bg='green',
                      fg='black', command=start_game, width=15, height=3)
    button_2 = Button(frame_2, text="Exit", anchor=CENTER, bg='red', fg='black', command=root.quit, width=15, height=3)

    frame_1.grid(row=0, column=0, sticky=W+E)
    frame_2.grid(row=1, column=0, sticky=W+E)
    label.grid(row=0, column=0)
    button_1.grid(row=0, column=0, sticky=N)
    button_2.grid(row=1, column=0, sticky=S)

    root.mainloop()
