import tkinter

class Error(tkinter.Frame):
    def __init__(self, parent: tkinter.Tk) -> None:
        super().__init__(parent)

        tkinter.Label(text = "Something is wrong").pack()
