from tkinter import *


def back():
    pass

root = Tk()
framenav = Frame(root)
framenav.pack(fill=X)
Button(framenav, text='Hinzufügen', command=back, padx=10).pack(pady=4, padx=10, side=RIGHT)
S = Scrollbar(root)
T = Text(root)
S.pack(side=RIGHT, fill=Y)
# T.pack(side=LEFT, fill=BOTH)
T.pack(fill=BOTH)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)


root.mainloop()