from window import Window
from items import Line, Point
from cell import Cell
        

def main():
    window = Window(800, 600)
    line = Line(Point(100, 100), Point(200, 600))
    window.draw_line(line, "red")
    cell = Cell(window.canvas, 300, 300, 100, 100)
    window.draw_cell(cell)
    window.wait_for_close()

if __name__ == "__main__":
    main()
        