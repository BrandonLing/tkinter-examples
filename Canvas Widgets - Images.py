from Tkinter import *

canvas_width = 1000
canvas_height =600

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="test.gif")
canvas.create_image(20,20, anchor=NW, image=img)

mainloop()