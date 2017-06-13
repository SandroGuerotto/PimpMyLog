from tkinter import *


class Navigation:

    def __init__(self, framenav, controller):
        # instanzvariable = self.<name>
        self.framenav = framenav
        self.controller = controller

        Label(framenav, text="Genutzer Speicherplatz: ").pack(padx=10, side=LEFT)
        self.usage = Label(framenav)
        self.usage.pack(side=LEFT)

        # placeholder
        Label(framenav, text="").pack(padx=50, side=LEFT)

        Label(framenav, text="Anzahl Dateien:").pack(padx=10, side=LEFT)
        self.filecount = Label(framenav)
        self.filecount.pack(side=LEFT)

        # placeholder
        Label(framenav, text="").pack(padx=10, side=LEFT)

        Button(framenav, text='Löschen', command=self.delete).pack(pady=4, padx=10, side=RIGHT)
        Button(framenav, text='Hinzufügen', command=self.add, padx=10).pack(pady=4, padx=10, side=RIGHT)

    def delete(self):
        self.controller.delete()

    def add(self):
        self.controller.add()

    def set_usage(self, size):
        self.usage.config(text=size)

    def set_file_count(self, count):
        self.filecount.config(text=count)



