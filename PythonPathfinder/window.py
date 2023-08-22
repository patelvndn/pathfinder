from tkinter import *
from main.uiManager import *

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

root = Tk()
root.title('Python Pathfinder')
root.geometry("800x800")

manager = Manager(root)

root.mainloop()

