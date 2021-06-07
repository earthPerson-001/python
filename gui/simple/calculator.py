from tkinter import *

first_number = ''
second_number = ''
list_1 = []
root = Tk()

root.title("simple calculator")
e = Entry(root, width=40, borderwidth=5)


def click_button(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def button_add():
    global first_number
    first_number = e.get()
    e.delete(0, END)


def button_clear():
    global first_number, second_number
    first_number = ''
    second_number = ''
    e.delete(0, END)


def button_delete():
    current = e.get()
    global list_1
    for i in range(len(current)-1):
        list_1.append(current[i])
    e.delete(0, END)
    e.insert(0, ''.join(list_1))
    list_1 = []


def button_equal_to():
    while e.get() == "" or type(int(e.get())) != int:
        root.title("simple calculator-please enter valid digit")
    global second_number
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, int(first_number) + int(second_number))


# defining button
button_1 = Button(root, text="1", padx=30, pady=10, command=lambda: click_button(1))
button_2 = Button(root, text="2", padx=30, pady=10, command=lambda: click_button(2))
button_3 = Button(root, text="3", padx=30, pady=10, command=lambda: click_button(3))
button_4 = Button(root, text="4", padx=30, pady=10, command=lambda: click_button(4))
button_5 = Button(root, text="5", padx=30, pady=10, command=lambda: click_button(5))
button_6 = Button(root, text="6", padx=30, pady=10, command=lambda: click_button(6))
button_7 = Button(root, text="7", padx=30, pady=10, command=lambda: click_button(7))
button_8 = Button(root, text="8", padx=30, pady=10, command=lambda: click_button(8))
button_9 = Button(root, text="9", padx=30, pady=10, command=lambda: click_button(9))
button_0 = Button(root, text="0", padx=30, pady=10, command=lambda: click_button(0))

button_add = Button(text="+", padx=70, pady=10, command=button_add)
button_clear = Button(text="clear", padx=30, pady=10, command=button_clear)
button_equal_to = Button(text="=", padx=30, pady=10, command=button_equal_to)
button_del = Button(root, text="del", padx=30, pady=10, command=button_delete)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_equal_to.grid(row=5, column=0)
button_clear.grid(row=5, column=1)
button_del.grid(row=5, column=2)
button_add.grid(row=4, column=1, columnspan=2)

e.grid(row=0, column=0, columnspan=3)


root.mainloop()
