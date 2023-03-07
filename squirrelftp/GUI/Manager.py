from tkinter import Tk
from tkinter import Frame

from pages import *

class Manager(Tk):
    instance: 'Manager | None' = None

    def __init__(self) -> None:
        if Manager.instance is not None:
            raise Exception("This class is singleton!")

        super().__init__()

        self.title("Squireel FTP")

        self.resizable(False, False)

        self.container = Frame(self, height = 300, width = 300)
        self.container.pack()

        self.pages: dict[PagesList, Frame] = {
            PagesList.LOGIN: Login(self),
            PagesList.ERROR: Error(self),
        }

        for name in self.pages:
            self.pages[name].pack()

        Manager.instance = self

    @classmethod
    def get_instance(cls) -> 'Manager':
        if cls.instance is None:
            cls.instance = Manager()
        
        return cls.instance

    def to(self, page: PagesList) -> 'Manager':
        frame = self.pages.get(page)

        if frame is None:
            frame = self.pages[PagesList.ERROR]

        frame.tkraise()

        return self
    
if __name__ == "__main__":
    Manager.get_instance().to(PagesList.ERROR).mainloop()