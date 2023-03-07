import tkinter

class Login(tkinter.Frame):
    def __init__(self, parent: tkinter.Tk) -> None:
        super().__init__(parent)

        tkinter.Label(text = "P'agina de login").pack()
