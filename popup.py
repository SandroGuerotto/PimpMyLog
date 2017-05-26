from tkinter import *
from tkinter import filedialog


class PopupFile:

    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.focus_set()
        self.top.grab_set()
        # first row
        self.lbl_path = Label(self.top, text="Dateipfad:")
        self.lbl_path.grid(row=0, column=0, ipadx=30, pady=20)

        self.e_path = Entry(self.top,  width=80)
        self.e_path.grid(row=0, column=1, padx=0)
        self.btn_browse = Button(self.top, text="...", command=self.opendialog)
        self.btn_browse.grid(row=0, column=2, padx=10, ipadx=5)

        Label(self.top, text="").grid(row=0, column=3, padx=20)

        # second row
        self.lbl_name = Label(self.top, text="Name:")
        self.lbl_name.grid(row=1, column=0, ipadx=30)

        self.e_name = Entry(self.top, width=80)
        self.e_name.grid(row=1, column=1, columnspan=2, padx=0, sticky=W)

        Label(self.top, text="").grid(row=1, column=3, padx=20)

        # thrid row
        self.btn_cancel = Button(self.top, text='Abbrechen', command=self.cancel)
        self.btn_cancel.grid(row=2, column=0, padx=30, pady=20)

        self.btn_submit = Button(self.top, text="Hinzufügen", command=self.cancel)
        self.btn_submit.grid(row=2, column=2, sticky=E)

    def show(self):
        self.top.mainloop()

    def cancel(self):
        self.top.grab_release()
        self.top.quit()

    def getattr(self):
        return self.e_path.get(), self.e_name.get()

    def opendialog(self):
        filename = filedialog.askopenfilename(parent=self.top)
        self.e_path.insert(0, filename)
