from tkinter import *
import numpy as np

class MyGrid(Canvas):
    def __init__(self, parent, size, **kw):
        super(MyGrid, self).__init__(parent, width=size[0], height=size[1], **kw)
        self.width = size[0]
        self.height = size[1]
        self.gsize = size
        self.startTile = None
        self.endTile = None

    def drawRectangle(self, gridPoint, cornerPoint, size, color, outline_color, outline_width):
        rectObject = self.create_rectangle(
                                 cornerPoint[0],
                                 cornerPoint[1],
                                 cornerPoint[0]+size[0], 
                                 cornerPoint[1]+size[1], 
                                 fill=color, 
                                 outline=outline_color, 
                                 width=outline_width, 
                                 tags="rect")
        self.objectToPosition[rectObject] = gridPoint
        self.positionToObject[gridPoint] = rectObject

    def clear(self):
        for x in self.find_withtag("rect"):
            gx, gy = self.objectToPosition[x]
            self.setRectGrid(gx, gy,  "open")

    def setRect(self, x, y, tag):
        if (not self._positionInGrid(x,y)): return
        item = self.find_closest(x, y)[0]
        gx, gy = self.objectToPosition[item]
        self._setCube(item, gx, gy, tag)

    def setRectGrid(self, x, y, tag):
        if(not (x,y) in self.positionToObject.keys()): return
        item = self.positionToObject[(x,y)]
        self._setCube(item, x, y, tag)

    def _setCube(self, cube, x, y, tag):
        if tag == "obstacle":
            self.occupancy[x,y] = 1
            self.itemconfig(cube, fill='black')
        if tag == "open":
            self.occupancy[x,y] = 0 
            self.itemconfig(cube, fill='white')
        if tag == "path":
            self.itemconfig(cube, fill='lightblue')
        if tag == "start":
            if (self.startTile):
                self.itemconfig(self.startTile[1], fill='white')
            self.startTile = ((x,y),cube)
            self.itemconfig(cube, fill='green')
        if tag == "end":
            if (self.endTile):
                self.itemconfig(self.endTile[1], fill='white')
            self.endTile = ((x,y),cube)
            self.itemconfig(cube, fill='red')

    def _positionInGrid(self, x, y):
        if (x > self.maxPoint[0] or 
        x < self.minPoint[0] or
        y > self.maxPoint[1] or 
        y < self.minPoint[1]): return False
        return True

    def printOccupancy(self):
        print(self.occupancy)

    def initialize(self, dimensions, offset, pad):
        self.dim = dimensions
        self.pad = pad
        self.offset = offset
        self.occupancy = np.zeros(dimensions)
        self.maxPoint = (self.gsize[0] - pad, self.gsize[1] - pad)
        self.minPoint = (pad, pad)
        self.objectToPosition = {}
        self.positionToObject = {}

    def drawSquares(self, fill="white", outline="black", outline_width=1):
        #declare size of a tile and size of a square inside that tile
        tile_size = ((self.width - 2 * self.pad) / self.dim[0], (self.height - 2 * self.pad) / self.dim[1])
        square_size = (tile_size[0] - 2 *self.offset[0], tile_size[1] - 2 *self.offset[1])

        #loop through all squares and draw them
        for x in range(0, self.dim[0]):
            for y in range(0, self.dim[1]):
                x1 = tile_size[0] * x + self.offset[0]
                y1 = tile_size[1] * y + self.offset[1]
                screenPoint = (x1 + self.pad, y1 + self.pad)
                gridPoint = (y,x) # this works... dont know why
                self.drawRectangle(gridPoint, screenPoint, square_size, fill, outline, outline_width)

        self.setRect(self.minPoint[0]+1, self.minPoint[1]+1, "start")
        self.setRect(self.maxPoint[0]-1, self.maxPoint[1]-1, "end")
