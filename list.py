from tkinter import *
from tkinter import ttk


class List:

    def __init__(self, listframe):
        self.listframe = listframe

        # set column
        self.tree = ttk.Treeview(listframe, columns=('name', 'logdata', 'date', 'size'))

        # set column name
        self.tree.heading('#0', text='ID')
        self.tree.column('#0', minwidth=50, width=50)

        self.tree.heading('#1', text='Name')
        self.tree.column('#1', minwidth=100, width=100)

        self.tree.heading('#2', text='Datei')
        self.tree.column('#2', minwidth=100, width=100)

        self.tree.heading('#3', text='Datum')
        self.tree.column('#3', minwidth=100, width=100)

        self.tree.heading('#4', text='Grösse')
        self.tree.column('#4', minwidth=100, width=100)

        # return tree object
        self.gettree()

    def insert_data(self, id, progname, name, date, size):
        self.tree.insert('', 'end', text=id, value=(progname, name, date, size))

    def gettree(self):
        self.tree.pack(fill=X)
        return self.tree
