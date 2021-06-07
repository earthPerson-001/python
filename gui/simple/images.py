from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("photo-1531804055935-76f44d7c3621.jpg")

quit_button = Button(root, text="Quit button", command=root.quit)

road_img = ImageTk.PhotoImage(Image.open("photo-1531804055935-76f44d7c3621.jpg"))

road_image = Label(image=road_img)

road_image.pack()

quit_button.pack()

root.mainloop()
