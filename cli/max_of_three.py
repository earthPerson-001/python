def max_of_three(a, b, c):
    if a > b and a > c:
        print(a, " is the greatest")
    elif b > a and b > c:
        print(b, " is the greatest")
    elif c > a and c > b:
        print(c, " is the greatest")


max_of_three(1, 2, 3)

def max1(iterables):
    iterables = sorted(iterables)
    print(iterables[-1])


a = [1, 5, 8, 15, 2, 3]
max1(a)

