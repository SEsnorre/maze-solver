from tkinter import Tk, BOTH, Canvas
from items import Line
from cell import Cell

class Window(Tk):
    
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title="My Window"
        self.canvas = Canvas(self.root_widget, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            
    def close(self):
        self.running = False
        
    def draw_line(self, line: Line, fill_color: str = "white", width: int = 2):
        line.draw(self.canvas, fill_color, width)
        
    def draw_cell(self, cell: Cell, fill_color: str = "black", width: int = 2):
        cell.draw(fill_color, width)
        
    