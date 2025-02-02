from tkinter import Canvas
from items import Line, Point

class Cell():
    
    def __init__(self, canvas: Canvas, x, y, width, height):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._walls = [self.has_top_wall, self.has_right_wall, self.has_bottom_wall, self.has_left_wall]
        
        self.visited = False
        
        self._x1 = x
        self._y1 = y
        self._x2 = x + width
        self._y2 = y + height
        self._edges = [Point(self._x1, self._y1), Point(self._x2, self._y1), Point(self._x2, self._y2), Point(self._x1, self._y2)]
        
        if canvas is None:
            raise ValueError("Canvas not set")
        self._can = canvas
        
    def draw(self, fill_color: str = "black", width: int = 2):
        for i in range(4):
            line = Line(self._edges[i], self._edges[(i + 1) % 4])
            if self._walls[i]:
                line.draw(self._can, fill_color, width)
            else:
                line.draw(self._can, "#d9d9d9", width)
    
    def draw_move(self, to_cell, undo=False):
        if self._edges == to_cell._edges:
            return
        if undo:
            line_color = "grey"
        else:
            line_color = "red"
        center_from = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        center_to = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        
        if center_to.x > center_from.x and not self._walls[1]:
            line = Line(center_from, center_to)
            line.draw(self._can, line_color)
        elif center_to.x < center_from.x and not self._walls[3]:
            line = Line(center_from, center_to)
            line.draw(self._can, line_color)
        elif center_to.y > center_from.y and not self._walls[2]:
            line = Line(center_from, center_to)
            line.draw(self._can, line_color)
        elif center_to.y < center_from.y and not self._walls[0]:
            line = Line(center_from, center_to)
            line.draw(self._can, line_color)    
        else:
            raise ValueError("Invalid move")