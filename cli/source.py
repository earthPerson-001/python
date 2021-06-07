# python learning(basics)
if __name__ == "__main__":

    # hello world
    print("hello world!")  # prints hello world!
    print("hello \nworld")  # prints
    # hello
    # world
    print("hello \tworld")  # prints hello    world

    # assigning variables and using operators.
    a = 1
    b = 2
    print(a + b)

    # operating with strings
    a = "hello "  # there is a space after "o".
    b = "WORLD"
    c = "!"
    print(a + b + c)  # this operation combines strings without space.
    print(a.index("l"))  # this outputs the position of the first "l" in the string starting with 0.
    print(b.replace('W', 'F', 1))  # this replaces "w" of "world" with "f.
    print(a.count("l"))  # this counts the number of "l" in "hello " including spaces.
    print(a.upper())  # this prints strings of variable a in uppercase.
    print(b.lower())  # this prints the letters of the string "world" in lower case.
    print(a.isalpha())  # this checks whether a is alphabet logically.
    # this gives false as there is a space after "o".
    print(b.isalnum())  # this checks whether b is a number.

    # taking input from the user
    A = input("enter the first number: ")
    B = input("enter the second number: ")
    a = float(A)
    b = float(B)
    # input converts entered numbers to strings so "int" or "float" is used to convert them back to numbers
    print("the sum of {0} and {1} is {2}".format(a, b, a + b))
    # .format is used for formatting along with {} %s, %d, %.xf can also be used to format where %s denotes strings,
    # %d denotes digit/numbers, %.xf denotes a floating point number with x digits after decimal point
    print("the %s of %.5f and %.6f is approximately %d" % ("sum", a, b, a + b))
