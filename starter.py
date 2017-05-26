from list import *
from navigation import *
from popup import *
from tkinter import messagebox


class Controller:

    def __init__(self, main):
        self.main = main
        # create navigation bar
        self.framenav = Frame(main)
        self.framenav.pack(fill=X)
        self.nav = Navigation(self.framenav, self)
        # set filecount an memory usage
        self.nav.setfilecount(1)
        self.nav.setusage("5222KB")

        # create treeview
        self.listframe = Frame(main)
        self.listframe.pack(fill=X)
        self.list = List(self.listframe)
        self.list.gettree().bind("<Double-1>", self.OnDoubleClick)

    def delete(self):
        # get treeview
        tree = self.list.gettree()
        # check if an item is selected
        if tree.selection():
            # show popup to confirm
            if messagebox.askokcancel("Logdatei entfernen", "Logdatei wirklich aus dem Programm entfernen?"):
                # loop at selection and delete items
                for selected in tree.selection():
                    tree.delete(selected)
                # toDo: delete from file

    def add(self):
        addpopup = PopupFile(self.main)
        addpopup.show()
        path, name = addpopup.getattr()
        addpopup.top.destroy()
        # toDo: add new Logfile to file
        print(path, name)

    def inserttolist(self):
        self.list.insert_data(12, "testprog", "test", "2016.02.15", "5222KB")
        self.list.insert_data(13, "testprog", "test", "2016.02.15", "5222KB")
        self.list.insert_data(14, "testprog", "test", "2016.02.15", "5222KB")

    def OnDoubleClick(self, event=None):
        item = self.list.gettree().focus()
        print(item)
        # toDo: setup log screen and load logfile into textarea

root = Tk()
root.title("PimpMyLog")
controller = Controller(root)
controller.inserttolist()

mainloop()
