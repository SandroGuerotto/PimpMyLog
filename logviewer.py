from site import ENABLE_USER_SITE
from tkinter import *


class Logviewer:
    def __init__(self, root, name, content):
        self.top = Toplevel(root)
        self.top.focus_set()
        self.top.grab_set()
        # setup navigation bar
        self.framenav = Frame(self.top)
        self.framenav.pack(fill=X)
        self.lbl_name = Label(self.framenav, text="Dateiname")
        self.lbl_name.pack(padx=10, side=LEFT)

        Button(self.framenav, text='Zurück', command=self.back, padx=10).pack(pady=4, padx=10, side=RIGHT)

        # logviewer with scrollbar
        scrollbar = Scrollbar(self.top)
        self.textarea = Text(self.top, width=150, height=35)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.textarea.pack(fill=BOTH)
        scrollbar.config(command=self.textarea.yview)

        # bind scrollbar to textarea
        self.textarea.config(yscrollcommand=scrollbar.set)

        # set content
        self.set_name(name)
        self.set_text(content)

    def back(self):
        #return to main Screen
        self.top.grab_release()
        self.top.destroy()

    def set_text(self, text):
        # set log content to textarea
        self.textarea.config(state=NORMAL)
        self.textarea.insert(INSERT, text)
        self.textarea.config(state=DISABLED)

    def set_name(self, name):
        self.lbl_name.config(text=name)
