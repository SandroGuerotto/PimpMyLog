from tkinter import *
from tkinter import ttk

class List:
    tree = None

    def __init__(self, listframe):
        self.listframe = listframe

        # set column
        List.tree = ttk.Treeview(listframe, columns=('name', 'logdata', 'date',  'size'))

        # set column name
        List.tree.heading('#0', text='ID')
        List.tree.column('#0', minwidth=50, width=50)
        List.tree.heading('#1', text='Name')
        List.tree.heading('#2', text='Datei')
        List.tree.heading('#3', text='Datum')
        List.tree.heading('#4', text='Grösse')

        # return tree object
        self.getTree()

    def insert_data(self, id, progname, name, date, size):
        List.tree.insert('', 'end', text=id,  value=(progname,name,date,size))

    def getTree(self):
        List.tree.pack(fill=X)
        return List.tree

