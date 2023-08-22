import tkinter as tk
'''
to find out what you can do with a certain tkinter object...
	btn = ttk.Button(frm, ...)
	print(btn.configure().keys())

or you can compare what methods a certain object has
	print(set(btn.configure().keys()) - set(frm.configure().keys()))

or print every option!
	print(dir(btn))
	print(set(dir(btn)) - set(dir(frm)))
'''


class AlgorithmSelection(tk.OptionMenu):
    def __init__(self, master):
        options = [
            "Dijkstras",
            "A*",
            "Depth First Search",
            "Bredth First Search"
        ]
        clicked = tk.StringVar()
        self.menuValue = options[3]
        clicked.set(self.menuValue)

        tk.OptionMenu.__init__(self, master, clicked, command=self._update_value, *options)

        self.config(width=20)
        self.clicked = clicked

    def _update_value(self, selection):
        self.menuValue=selection

    def getValue(self):
        return str(self.menuValue)
        
        
