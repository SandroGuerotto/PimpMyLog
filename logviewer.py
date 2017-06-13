from tkinter import *


class Logviewer:
    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.focus_set()
        self.top.grab_set()
        # setup navigation bar
        self.framenav = Frame(self.top)
        self.framenav.pack(fill=X)
        Label(self.framenav, text="Dateiname").pack(padx=10, side=LEFT)

        Button(self.framenav, text='Zurück', command=self.back, padx=10).pack(pady=4, padx=10, side=RIGHT)

        # logviewer with scrollbar
        scrollbar = Scrollbar(self.top)
        self.textarea = Text(self.top, width=150, height=35)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.set_text()
        self.textarea.pack(fill=BOTH)
        scrollbar.config(command=self.textarea.yview)
        # bind scrollbar to textarea
        self.textarea.config(yscrollcommand=scrollbar.set)
        self.textarea.config(state=DISABLED)

    def back(self):
        self.top.grab_release()
        self.top.destroy()

    def set_text(self):
        self.textarea.insert(END,
                             """[03/19/2017 21:43.53.326] WudfCoInstaller: Service WudfSvc is already running.
[03/19/2017 21:43.53.320] WudfCoInstaller: Configuring UMDF Service WpdMtpDriver.
[03/19/2017 21:43.53.320] WudfCoInstaller: Configuring UMDF Service WpdMtpDriver.
[03/19/2017 21:43.53.320] WudfCoInstaller: Configuring UMDF Service WpdMtpDriver.
[03/19/2017 21:43.53.320] WudfCoInstaller: Configuring UMDF Service WpdMtpDriver.
[03/19/2017 21:43.53.320] WudfCoInstaller: Configuring UMDF Service WpdMtpDriver.
[03/19/2017 21:43.53.322] WudfCoInstaller: ImpersonationLevel set to 2""")
