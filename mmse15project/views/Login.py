import tkinter as tk

__author__ = 'tobias'


class Login(tk.Frame):
    def __init__(self, ctrl, master=None):
        self.ctrl = ctrl
        tk.Frame.__init__(self, master)
        self.pack()
        self.auth()

    def auth(self):
        l1 = tk.Label(self, text="User:")
        l2 = tk.Label(self, text="Pass:")

        e1 = tk.Entry(self)
        e2 = tk.Entry(self, show="*")

        b1 = tk.Button(self, text="Login",
                       command=lambda:
                       self.ctrl.login_auth(self, e1.get(), e2.get()))

        l1.grid(row=0, sticky=tk.E)
        l2.grid(row=1, sticky=tk.E)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        b1.grid(columnspan=2)

    def fail(self):
        l1 = tk.Label(self, text="Authentication failed")
        b1 = tk.Button(self, text="Try again",
                       command=lambda: self.ctrl.login_try_again(self))
        b2 = tk.Button(self, text="Quit",
                       command=lambda: self.ctrl.login_quit())
        l1.grid(columnspan=2)
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
