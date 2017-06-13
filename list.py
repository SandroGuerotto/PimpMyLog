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

        self.tree.heading('#2', text='Dateipfad')
        self.tree.column('#2', minwidth=100, width=350)

        self.tree.heading('#3', text='Datum')
        self.tree.column('#3', minwidth=100, width=100)

        self.tree.heading('#4', text='Grösse')
        self.tree.column('#4', minwidth=100, width=100)

        # return tree object
        self.get_tree()

    def insert_data(self, id, progname, path, date, size):
        self.tree.insert('', 'end', text=id, value=(progname, path, date, size))

    def get_tree(self):
        self.tree.pack(fill=X)
        return self.tree
