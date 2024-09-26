from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()

print("about to call image")
img = Image.open("graphics/icon.png")
img = ImageTk.PhotoImage(img)
print("image called")
label = Label(root, image=img)
print("label created")
label.pack()

root.mainloop()
