from list import *
from navigation import *
from popup import *
from logviewer import *
from tkinter import messagebox
from dataloader import *


class Controller:

    def __init__(self, main):
        self.main = main
        self.usage = 0
        # create navigation bar
        self.framenav = Frame(main)
        self.framenav.pack(fill=X)
        self.nav = Navigation(self.framenav, self)

        # create treeview
        self.listframe = Frame(main)
        self.listframe.pack(fill=X)
        self.list = List(self.listframe)
        # bind doubleclick on row
        self.list.get_tree().bind("<Double-1>", self.on_double_click)

        # dataloader
        self.loglist = read_logfile_list_from_file()
        for log in self.loglist:
            self.list.insert_data(log.id, log.name, log.path, log.date, log.size)

        # set filecount an memory usage
        self.update_gui()

    def delete(self):
        # get treeview
        tree = self.list.get_tree()
        # check if an item is selected
        if tree.selection():
            # show popup to confirm
            if messagebox.askokcancel("Logdatei entfernen", "Logdatei wirklich aus dem Programm entfernen?"):
                # loop at selection and delete items
                for selected in tree.selection():
                    id = tree.item(selected, "text")
                    tree.delete(selected)
                    i = 0
                    for log in self.loglist:
                        if log.id == id:
                            del self.loglist[i]
                        i = 1 + i
                self.update_gui()

    def add(self):
        # open add popup. splits return array into to variables to save into file
        addpopup = PopupFile(self.main)
        addpopup.show()

        # save entered values
        path, name = addpopup.get_attribute()
        addpopup.top.destroy()

        size, date, id = write_logfile_list_in_file(name, path)
        # insert new logfile into list
        self.list.insert_data(id, name, path, date, size)
        self.loglist = read_logfile_list_from_file()
        self.update_gui()

    def on_double_click(self, event=None):
        # read selected item, read data from file and display logs in textviewer
        item = self.list.get_tree().focus()
        name = self.list.get_tree().item(item)["values"][0]
        path = self.list.get_tree().item(item)["values"][1]
        content = get_logfile_content(path)
        Logviewer(self.main, name, content)

    def update_gui(self):
        # update GUI labels
        self.usage = 0
        for log in self.loglist:
            self.usage = self.usage + log.size

        self.nav.set_usage(self.usage)
        self.nav.set_file_count(len(self.loglist))


root = Tk()
root.title("PimpMyLog")
controller = Controller(root)

mainloop()
