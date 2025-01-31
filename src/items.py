import math
from tkinter import Canvas

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __pos__(self):
        return Point(+self.x, +self.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __invert__(self):
        return Point(~self.x, ~self.y)

    def __round__(self, n):
        return Point(round(self.x, n), round(self.y, n))

    def __floor__(self):
        return Point(math.floor(self.x), math.floor(self.y))

    def __ceil__(self):
        return Point(math.ceil(self.x), math.ceil(self.y))

    def __trunc__(self):
        return Point(math.trunc(self.x), math.trunc(self.y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
        
        
class Line():
    
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        
    def draw(self, canvas: Canvas, fill_color: str, width: int = 2):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=width)

    def __str__(self):
        return f"({self.start} -> {self.end})"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.start, self.end))

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.start
        elif index == 1:
            return self.end
        else:
            raise IndexError("Index out of range")