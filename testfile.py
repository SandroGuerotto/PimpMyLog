from tkinter import *
from tkinter import ttk


class List:
    tree = None

    def __init__(self, listframe):
        self.listframe = listframe

        # set column
        List.tree = ttk.Treeview(listframe, columns=('id,''name', 'logdata', 'date',  'size'))
        List.tree['columns'] = ('id','name', 'logdata', 'date',  'size')
        List.tree.column('size', width=100, anchor='center')

        # set column name
        List.tree.heading('id', text='ID')
        List.tree.heading('name', text='Name')
        List.tree.heading('logdata', text='Datei')
        List.tree.heading('date', text='Datum')
        List.tree.heading('size', text='Grösse')

        # return tree object
        self.getTree()

    def insert_data(self, progname, name, date, size):
        # Inserted at the root, program chooses id:
        List.tree.insert('', 'end', 'widgets', text='Widget Tour')

    def getTree(self):
        List.tree.pack(fill=X)
        return List.tree



def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))


root = Tk()
count = 3
framenav = Frame(root)
framenav.pack(fill=X)

Label(framenav, text="Genutzer Speicherplatz: ").pack(padx=10, side=LEFT)
usage = Label(framenav, text="1524KB").pack(side=LEFT)

# placeholder
Label(framenav, text="").pack(padx=50, side=LEFT)

Label(framenav, text="Anzahl Dateien:").pack(padx=10, side=LEFT)
filecount = Label(framenav, text=str(count)).pack(side=LEFT)

# placeholder
Label(framenav, text="").pack(padx=10, side=LEFT)

Button(framenav, text='Löschen', command=root.quit).pack(pady=4, padx=10, side=LEFT)
Button(framenav, text='Hinzufügen', command=show_entry_fields, padx=10).pack(pady=4, padx=10, side=LEFT)

listframe = Frame(root)
listframe.pack(fill=X, side=BOTTOM)
list = List(listframe)

list.insert_data("testprog", "test", "2016.02.15", "5222KB")
# tree = ttk.Treeview(listframe, columns=('name', 'size', 'modified'))
# tree['columns'] = ('name', 'size', 'modified', 'owner')
# tree.column('size', width=100, anchor='center')
# tree.heading('size', text='Size')
# tree.heading('name', text='Name ')
#
# # Inserted at the root, program chooses id:
# tree.insert('', 'end', 'widgets', text='Widget Tour')
#
# # Same thing, but inserted as first child:
# tree.insert('', 0, 'gallery', text='Applications')
#
# tree.pack(fill=X)

# listbox = Listbox(listframe)
# listbox.pack(fill=X)
# listbox.insert(END, "a list entry")
#
#
# for item in ["one", "two", "three", "four"]:
#     listbox.insert(END, item)


mainloop()

