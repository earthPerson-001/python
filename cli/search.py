from time import *
program = "y"

while program == "y":
    t = time()

    def linear_search(lst, a):
        for i in lst:
            if i == a:
                return True
        return False


    def binary_search(lst, a):
        lst = sorted(lst)
        lower = 0
        upper = len(lst) - 1

        while lower <= upper:
            mid = (lower + upper) // 2

            if lst[mid] == a:
                return True
            else:
                if lst[mid] < a:
                    lower = mid + 1
                else:
                    upper = mid - 1
        return False


    numbers = [1, 2, 3, 5, 6, 2426, 9709, 1010, 1111]
    b = int(input("enter the number"))

    method = int(input("enter the search method: \n1) binary \n2) linear \n 1 or 2 :"))

    if method == 1:
        search = binary_search(numbers, b)
    else:
        search = linear_search(numbers, b)
    if search:
        c = str(numbers.count(b))
        d = numbers.count(int(b))
        pos = numbers.index(b) + 1
        if d == 1:
            r = "is"
        else:
            r = "are"
        print("There %s {1} '{2}' in the list at %s position".format(r, c, b) % (r, pos))
    else:
        print("There is no {0} in the list".format(b))
    input("press Enter to continue(The program will terminate after 1 minute of inactivity)")

    program = "Terminate"
    if time() - t < 60:
        program = input("do you wish to continue the search?:(y/n)\n")
    else:
        print("The program has been terminated due to inactivity.")

