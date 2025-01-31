import unittest

from maze import Maze
from window import Window

class TestMaze(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Window(800, 800), 0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Window(800, 800), 0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0]._walls[3])
        self.assertFalse(m1._cells[num_rows - 1][num_cols - 1]._walls[2])

if __name__ == '__main__':
    unittest.main()