from tkinter import *


class Navigation:
    usage = None
    filecount = None

    def __init__(self, framenav):
        self.framenav = framenav

        Label(framenav, text="Genutzer Speicherplatz: ").pack(padx=10, side=LEFT)
        Navigation.usage = Label(framenav)
        Navigation.usage.pack(side=LEFT)

        # placeholder
        Label(framenav, text="").pack(padx=50, side=LEFT)

        Label(framenav, text="Anzahl Dateien:").pack(padx=10, side=LEFT)
        Navigation.filecount = Label(framenav)
        Navigation.filecount.pack(side=LEFT)

        # placeholder
        Label(framenav, text="").pack(padx=10, side=LEFT)

        Button(framenav, text='Löschen', command=self.delete()).pack(pady=4, padx=10, side=RIGHT)
        Button(framenav, text='Hinzufügen', command=self.add(), padx=10).pack(pady=4, padx=10, side=RIGHT)

    def add(self):
        pass
        # open file picker

    def delete(self):
        pass

    def setusage(self, size):
        Navigation.usage.config(text=size)

    def setfilecount(self, count):
        Navigation.filecount.config(text=count)
