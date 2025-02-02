from window import Window
from items import Line, Point
from cell import Cell
from maze import Maze
        

def main():
    num_rows = 50
    num_cols = 50
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(win, margin, margin, num_rows, num_cols, cell_size_x, cell_size_y)
    if maze.solve():
        print("path found")
    else:
        print("no path found")

    win.wait_for_close()
    
if __name__ == "__main__":
    main()
        