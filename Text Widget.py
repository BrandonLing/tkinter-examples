from Tkinter import *

root = Tk()

text1 = Text(root, height=35, width=80)
photo=PhotoImage(file='./test.gif')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042',
						font=('Tempus Sans ITC', 12, 'bold'))
text2.tag_bind('move', '<1>', lambda e, t=text2: t.insert(END, "Move it!"))
text2.insert(END,'\nWilliam Shakespeare\n', 'big')
quote = """
I like to move it move it.
I like to move it move it.
I like to... MOVE IT!
"""
text2.insert(END, quote, 'color')
text2.insert(END, 'move-it\n', 'move')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()