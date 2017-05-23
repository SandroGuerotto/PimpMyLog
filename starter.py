from list import *
from navigation import *
from tkinter import *

root = Tk()

framenav = Frame(root)
framenav.pack(fill=X)
nav = Navigation(framenav)
nav.setfilecount(1)
nav.setusage("5222KB")

listframe = Frame(root)
listframe.pack(fill=X)
list = List(listframe)

list.insert_data(12, "testprog", "test", "2016.02.15", "5222KB")

mainloop()





