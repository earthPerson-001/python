import random


def guess_the_number():
    start_game = "y"
    while start_game == "y":
        guess = int(input("Guess the number:\n"))
        n = random.randint(1, 11)
        continue_game = "y"
        while continue_game == "y":
            if n == guess:
                print("yes", n, "was the number that this computer was thinking")
                start_game = input("Do you want to start new game? y/n").lower()
                break
            else:
                print("sorry, incorrect")
                continue_game = input(" Do you want to continue guessing? y/n ").lower()
                if guess < n:
                    print("Guess higher")
                else:
                    print("Guess lower")
            guess = int(input(":"))



guess_the_number()
