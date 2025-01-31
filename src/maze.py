from cell import Cell
from window import Window
from time import sleep
import random


class Maze():
    def __init__(self, win: Window, x1,y1, num_rows, num_cols, cell_width, cell_height, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            self._seed = random.seed(seed)
        else:
            self._seed = random.seed()
            
    def _create_cells(self):               
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._win.canvas, self._x1 + j * self._cell_width, self._y1 + i * self._cell_height, self._cell_width, self._cell_height)
                row.append(cell)
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j,0)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
            
    def _draw_cell(self, row, col, speed=50):
        self._cells[row][col].draw()
        self._animate(speed)
        
    def _animate(self, speed):
        self._win.redraw()
        sleep(0 if speed == 0 else speed)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0]._walls[3] = False
        self._cells[self._num_rows - 1][self._num_cols - 1]._walls[2] = False
        self._draw_cell(0, 0,0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1,0)
    
    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        while 1:
            n = [(row-1,col),(row, col-1),(row, col+1),(row+1,col)]
            possible_neighbors = list(filter(lambda x: x[0] in range(self._num_rows) and x[1] in range(self._num_cols), n))
            not_visited_neigh = list(filter(lambda x: not self._cells[x[0]][x[1]].visited, possible_neighbors))
            
            if len(not_visited_neigh) == 0:
                self._draw_cell(row,col,0)
                return
            r = random.randint(0,len(not_visited_neigh)-1)
            neighbor = not_visited_neigh[r]
            if neighbor[0] == row:
                if neighbor[1] < col:
                    self._cells[row][col]._walls[3] = False
                    self._cells[neighbor[0]][neighbor[1]]._walls[1] = False
                else:
                    self._cells[row][col]._walls[1] = False
                    self._cells[neighbor[0]][neighbor[1]]._walls[3] = False
            elif neighbor[1] == col:
                if neighbor[0] < row:
                    self._cells[row][col]._walls[0] = False
                    self._cells[neighbor[0]][neighbor[1]]._walls[2] = False
                else:
                    self._cells[row][col]._walls[2] = False
                    self._cells[neighbor[0]][neighbor[1]]._walls[0] = False
            self._draw_cell(row,col,0)
            self._draw_cell(neighbor[0],neighbor[1],0)
            self._break_walls_r(neighbor[0], neighbor[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False
            
                