import Tkinter as TK
import glob
import os
from PIL import ImageTk, Image


print(TK.__version__)

HexChars = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
i = 'glendale_hoppers_ffffff_1b1718.png'

def IsHex(str):
    for letter in str:
        if letter not in HexChars:
            return False
    return True


def greet():
    print("Greetings!")

root = TK.Tk()
root.geometry('1000x1000')


master = root
master.title("A simple GUI")

scrollbar = TK.Scrollbar(master)
scrollbar.pack(side=TK.RIGHT, fill=TK.Y)

label = TK.Label(master, text="This is our first GUI!")
label.pack()

#pilImage = Image.open(i)
#pilImage.show()
#image = ImageTk.PhotoImage(pilImage)
#TK.Label(root, image=image).pack()

greet_button = TK.Button(master, text="Greet", command=greet)
greet_button.pack()

close_button = TK.Button(master, text="Close", command=master.quit)
close_button.pack()

e1 = TK.Entry(master)
e2 = TK.Entry(master)
e1.pack()

img = ImageTk.PhotoImage(Image.open(i))
panel = TK.Label(master, image=img)
panel.pack()



root.mainloop()



