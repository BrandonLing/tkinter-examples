from Tkinter import *
from tkFileDialog import askopenfilename


def callback():
    name = askopenfilename()
    print name


errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()