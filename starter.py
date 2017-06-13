from list import *
from navigation import *
from popup import *
from logviewer import *
from tkinter import messagebox


class Controller:

    def __init__(self, main):
        self.main = main
        # create navigation bar
        self.framenav = Frame(main)
        self.framenav.pack(fill=X)
        self.nav = Navigation(self.framenav, self)
        # set filecount an memory usage
        self.nav.set_file_count(1)
        self.nav.set_usage("5222KB")

        # create treeview
        self.listframe = Frame(main)
        self.listframe.pack(fill=X)
        self.list = List(self.listframe)
        self.list.get_tree().bind("<Double-1>", self.on_double_click)

    def delete(self):
        # get treeview
        tree = self.list.get_tree()
        # check if an item is selected
        if tree.selection():
            # show popup to confirm
            if messagebox.askokcancel("Logdatei entfernen", "Logdatei wirklich aus dem Programm entfernen?"):
                # loop at selection and delete items
                for selected in tree.selection():
                    tree.delete(selected)
                # toDo: delete from file

    def add(self):
        # open add popup. splits return array into to variables to save into file
        addpopup = PopupFile(self.main)
        addpopup.show()
        path, name = addpopup.get_attribute()
        addpopup.top.destroy()
        # toDo: add new Logfile to file
        print(path, name)

    def insert_to_list(self):
        self.list.insert_data(12, "testprog", "test", "2016.02.15", "5222KB")
        self.list.insert_data(13, "testprog", "test", "2016.02.15", "5222KB")
        self.list.insert_data(14, "testprog", "test", "2016.02.15", "5222KB")

    def on_double_click(self, event=None):
        # read selected item, read data from file and display logs in textviewer
        item = self.list.get_tree().focus()
        print(self.list.get_tree().item(item))
        # toDo: setup log screen and load logfile into textarea
        Logviewer(self.main)


root = Tk()
root.title("PimpMyLog")
controller = Controller(root)
controller.insert_to_list()

mainloop()
