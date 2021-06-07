import random
# global variables
final_Number = []
user_Number_in_list = []
computer_Number = " "
user_Number = 'user Number'
Bull = 0
cows = 0
contd = ""


def input_the_number():  # takes the input from the user as a string and makes a list of those digits.
    global user_Number_in_list, user_Number
    user_Number = input('Enter a four digit number')
    user_Number_in_list = list(user_Number)


def computer_number():  # generates a list of random numerical strings.
    global final_Number, computer_Number
    for i in range(4):
        num = str(random.randint(0, 9))
        final_Number.append(num)
        computer_Number = ''.join(final_Number)


def to_find_cows_and_bulls(final_number, user_number_in_list):  # logic for cows and bulls.
    global Bull, cows
    for j in range(len(final_number)):
        for i in range(len(user_number_in_list)):
            if final_number[j] == user_number_in_list[i]:
                if i == j:
                    cows += 1
                else:
                    Bull += 1


def printing(user_number, bulls, cow):  # prints the number of cows and bulls
    print(user_number)
    print("Bulls=", bulls)
    print("Cows=", cow)


def cows_and_bulls_game():  # the game
    computer_number()
    c = 1
    global contd, cows, Bull
    if final_Number != user_Number:
        Bull = 0
        cows = 0
        while contd != "n":  # checks if user wishes to continue.   (needs tweaking), (not working)
            input_the_number()
            to_find_cows_and_bulls(final_Number, user_Number_in_list)
            printing(user_Number, Bull, cows)
            contd = str(input("Do you want to continue guessing? (y/n)")).lower
            c += 1

    def turn(d):
        if d == 1:
            return "st"
        elif d == 2:
            return "nd"
        elif d == 3:
            return "rd"
        else:
            return "nth"

    if computer_Number == user_Number:
        print("You have guessed correctly in {0} {1} attempt".format(c, turn(c)))
    else:
        print("You couldn't guess correctly in {0}{1} attempt".format(c, turn(c)))

    print("You have guessed {0} and the number is {1}".format(user_Number, computer_Number))


cows_and_bulls_game()  # calls the game
