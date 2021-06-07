from functools import partial
def multiply_generator(num):

    def multiplier(n):
        print(num * n)

    return multiplier


def sum(a, b):
    print(a + b)

multiplyby5 = multiply_generator(5)
multiplyby5(9)
multiplyby5(6)

multiplyby7 = multiply_generator(7)
multiplyby7(9)

add = partial(sum, 3)
add(2)