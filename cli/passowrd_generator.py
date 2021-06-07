from random import *

password = ''

def password_generator():
    global password
    secure = input("How strong you want your password to be ? ('weak' /'strong' /'very strong')").lower()
    length = int(input("input the desired length"))
    if secure == "weak":
        list_1 = "abcdefghijklmnopqrstuvwxyz"
        num = len(list_1)
        for i in range(length):
            password = password + list_1[randint(0, num-1)]
    elif secure == "strong":
        list_1 = "a1b2c3d4e5f6g7h8i9j0k!l@m#n$o%p^q&r*s(t)u_v+w=x~y.z<>,/?'"
        num = len(list_1)
        for i in range(length):
            password = password + list_1[randint(0, num-1)]
    else:
        list_1 = "a1b2c3d4e5f6g7h8i9j0k!l@m#n$o%p^q&r*s(t)u_v+w=x~y.z<>,/?':A*BCDEFG_-HIJKLMN`OPQRS{][]}TUVWXYZ"
        num = len(list_1)
        for i in range(length):
            password = password + list_1[randint(0, num-1)]

    print("Recommended password is: ", password)


password_generator()
