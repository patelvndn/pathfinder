from tkinter import *
class ClearBtn(Button):
    def __init__(self, root, **kw):
        super(ClearBtn, self).__init__(root, **kw)
        self.configure(command = self.clear)

    def bindCanvas(self, canvas):
        self.canvas = canvas

    def bindFunction(self, func):
        self.configure(command=lambda: [self.clear(), func()])

    def clear(self):
        self.canvas.clear()
