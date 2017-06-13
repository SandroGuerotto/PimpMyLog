from list import *
from navigation import *
from popup import *
from logviewer import *
from tkinter import messagebox
from dataloader import *


class Controller:

    def __init__(self, main):
        self.main = main
        self.id = 15
        # create navigation bar
        self.framenav = Frame(main)
        self.framenav.pack(fill=X)
        self.nav = Navigation(self.framenav, self)
        # set filecount an memory usage
        self.filecount = 3
        self.nav.set_file_count(self.filecount)
        self.usage = 7915
        self.nav.set_usage(self.usage)

        # create treeview
        self.listframe = Frame(main)
        self.listframe.pack(fill=X)
        self.list = List(self.listframe)
        # bind doubleclick on row
        self.list.get_tree().bind("<Double-1>", self.on_double_click)

        # dataloader
        self.loglist = read_logfile_list_from_file()

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

        # save entered values
        path, name = addpopup.get_attribute()
        addpopup.top.destroy()

        # toDo: add new Logfile to file
        write_logfile_list_in_file(name, path)
        # insert new logfile into list
        self.list.insert_data(self.id, name, path, "2017.06.13", "253KB")
        # ingrement id
        self.id = self.id + 1
        self.update_gui()

    def insert_to_list(self):
        # default data pump
        self.list.insert_data(12, "VMG install", "C:/Users/Sandro/Desktop/vmgcoinstall.log", "2016.02.15", "5222KB")
        self.list.insert_data(13, "WL2012", "C:/Windows/WL2012.log", "2013.11.13", "1498KB")
        self.list.insert_data(14, "Windows Update", "C:/Windows/WindowsUpdate.log", "2017.06.13", "1195KB")

    def on_double_click(self, event=None):
        # read selected item, read data from file and display logs in textviewer
        item = self.list.get_tree().focus()
        name = self.list.get_tree().item(item)["values"][0]
        path = self.list.get_tree().item(item)["values"][1]
        # toDo: setup log screen and load logfile into textarea
        content = get_logfile_content(path)
        Logviewer(self.main, name, content)

    def update_gui(self):
        # update GUI labels
        self.filecount = self.filecount + 1
        self.usage = self.usage + 253
        self.nav.set_file_count(self.filecount)
        self.nav.set_usage(self.usage)


root = Tk()
root.title("PimpMyLog")
controller = Controller(root)
controller.insert_to_list()

mainloop()
