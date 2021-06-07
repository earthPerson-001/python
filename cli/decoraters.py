def divider(a, b):
    print(a / b)


def correct_divider(func, a, b):
    if b > a:
        a, b = b, a
    return func(a, b)


correct_divider(divider, 1, 2)