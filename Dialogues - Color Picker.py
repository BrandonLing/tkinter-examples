from Tkinter import *
from tkColorChooser import askcolor


def callback():
    result = askcolor(color="#6A9662",
                      title="Bernd's Colour Chooser")
    print result


root = Tk()
Button(root,
       text='Choose Color',
       fg="darkgreen",
       command=callback).pack(side=LEFT, padx=10)
Button(text='Quit',
       command=root.quit,
       fg="red").pack(side=LEFT, padx=10)
mainloop()