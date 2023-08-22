from tkinter import *
from . import *
from .pathFinding.find import PathFinder
import threading

class Manager:
    def __init__(self, window):
        self.window = window
        self.gridInPixels = (500,500)
        self.my_canvas = None
        self._create_text()
        self._create_buttons()
        self._create_grid()
        self._bind_keys()

    def test(self):
        pass 

    def _create_text(self):
        canvas = Canvas(self.window, width=800, height = 100, bg="white")
        self.tutorial = canvas
        canvas.create_text(400,50,text="With your mouse over the square:\n    " + 
                                       "\"H\" to place start tile\n    " +
                                       "\"J\" to place goal tile\n    " + 
                                       "leftClick to place obstacles", fill="black")
        canvas.pack()


    def _create_buttons(self):
        self.buttonFrame = Frame(self.window)

        self.clearbtn = ClearBtn(self.buttonFrame, text='Clear')
        self.clearbtn.grid(column=0, row=0)
        self.clearbtn.bindFunction(self._clear)

        self.runbtn = RunBtn(self.buttonFrame, text='Find!', command= lambda: threading.Thread(target=self.runAlgorithm).start())
        self.runbtn.grid(column=2, row=0)

        self.dropDown = AlgorithmSelection(self.buttonFrame)
        self.dropDown.grid(column=3, row=0)
        
        self.buttonFrame.pack()

    def _clear(self):
        self._unbind_keys()
        self._bind_keys()

    def _create_grid(self):
        self.my_canvas = MyGrid(self.window, size = self.gridInPixels, bg='gray')
        self.my_canvas.pack(pady=20)
        self.window.update()
        self.my_canvas.initialize((10,10),(0,0),20) 
        self.my_canvas.drawSquares("white" , outline_width=1)

        self.clearbtn.bindCanvas(self.my_canvas)

    def _bind_keys(self):
        self.window.bind('<B1-Motion>', self.motion)
        self.window.bind('h', self.onH)
        self.window.bind('j', self.onJ)
        self.window.bind('t', self.test)
    def _unbind_keys(self):
        self.window.unbind('<B1-Motion>')
        self.window.unbind('h')
        self.window.unbind('j')

    def runAlgorithm(self):
        if self.my_canvas == None: return
        finder = PathFinder(self.my_canvas.occupancy)
        canv = self.my_canvas
        path = finder.find(self.my_canvas, self.dropDown.getValue(), canv.startTile[0], canv.endTile[0])
        self.colorPath(path)

    def colorPath(self, path):
        for x, y in path:
            if(self.my_canvas.startTile[0] == (x,y)): continue
            if(self.my_canvas.endTile[0] == (x,y)): continue
            current = (x, y)
            self.my_canvas.setRectGrid( current[0], current[1], "path" )
            

    def onJ(self, event):
        rooty = self.my_canvas.winfo_x()
        rootx = self.my_canvas.winfo_y()
        self.my_canvas.setRect(event.x - rootx, event.y - rooty, "end")
       
    def onH(self, event):
        rooty = self.my_canvas.winfo_x()
        rootx = self.my_canvas.winfo_y()
        self.my_canvas.setRect(event.x - rootx, event.y - rooty, "start")
 
    def motion(self, event):
        if (event.widget == self.my_canvas):
            self.my_canvas.setRect(event.x, event.y, "obstacle")
