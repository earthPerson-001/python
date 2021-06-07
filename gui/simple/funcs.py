from tkinter import *


def display_password_generator_frame():
    forget_frame()
    password_generator_frame.grid(row=0, column=0)


def display_saved_password_frame():
    forget_frame()
    saved_password_frame.grid(row=0, column=0)


def display_check_password_security_frame():
    forget_frame()
    password_generator_frame.grid(row=0, column=0)


def display_logout_messagebox():
    forget_frame()
    password_generator_frame.grid(row=0, column=0)


def display_vault_frame():
    forget_frame()
    password_generator_frame.grid(row=0, column=0)

def forget_frame():
    password_generator_frame.grid_forget()
    saved_password_frame.grid_forget()
    check_password_security_frame.grid_forget()
    logout_messagebox.grid_forget()
    vault_frame.grid_forget()


password_generator_frame = Frame(bg="cyan", height=400, width=400)
saved_password_frame = Frame(bg="maroon", height=400, width=400)
check_password_security_frame = Frame(bg="violet", height=400, width=400)
logout_messagebox = Frame(bg="blue", height=400, width=400)
vault_frame = Frame(bg="indigo", height=400, width=400)


