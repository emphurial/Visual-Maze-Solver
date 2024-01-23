from cell import Cell
from graphics import Window
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            current_row = []
            for j in range(self._num_rows):
                current_row.append(Cell(self._win))
            self._cells.append(current_row)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        last_cell = [self._num_rows - 1, self._num_cols - 1]
        self._cells[last_cell[1]][last_cell[0]].has_bottom_wall = False
        self._draw_cell(last_cell[1], last_cell[0])
    
    def _get_neighbours(self, i, j):
        neighbours = []
        #left neighbour
        if i > 0:
            neighbours.append([i - 1, j])
        #right neighbour
        if i < (self._num_cols - 1):
            neighbours.append([i + 1, j])
        #top neighbour
        if j > 0:
            neighbours.append([i, j - 1])
        #bottom neighbour
        if j < (self._num_rows - 1):
            neighbours.append([i, j + 1])
        return neighbours
    
    def _break_wall(self, i, j, target_i, target_j):
        if i > target_i:
            self._cells[i][j].has_left_wall = False
            self._cells[target_i][target_j].has_right_wall = False
        if i < target_i:
            self._cells[i][j].has_right_wall = False
            self._cells[target_i][target_j].has_left_wall = False
        if j > target_j:
            self._cells[i][j].has_top_wall = False
            self._cells[target_i][target_j].has_bottom_wall = False
        if j < target_j:
            self._cells[i][j].has_bottom_wall = False
            self._cells[target_i][target_j].has_top_wall = False


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            for neighbour in self._get_neighbours(i, j):
                x, y = neighbour
                if self._cells[x][y].visited == False:
                    to_visit.append(neighbour)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            target_cell = random.choice(to_visit)
            x, y = target_cell
            self._break_wall(i, j, x, y)
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        if self._solve_r(0, 0):
            return True
        return False
    
    def _wall_block(self, i, j, x, y):
        if i < x:
            if self._cells[i][j].has_right_wall or self._cells[x][y].has_left_wall:
                return False
        if i > x:
            if self._cells[i][j].has_left_wall or self._cells[x][y].has_right_wall:
                return False
        if j < y:
            if self._cells[i][j].has_bottom_wall or self._cells[x][y].has_top_wall:
                return False
        if j > y:
            if self._cells[i][j].has_top_wall or self._cells[x][y].has_bottom_wall:
                return False
        return True
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        for direction in self._get_neighbours(i, j):
            x, y = direction
            if self._cells[x][y].visited == False and self._wall_block(i, j, x, y):
                Cell.draw_move(self._cells[i][j], self._cells[x][y])
                if self._solve_r(x, y):
                    return True
                Cell.draw_move(self._cells[i][j], self._cells[x][y], undo = True)           
        return False
            

            

        
            



    def _animate(self):
        if self._win == None:
            return
        Window.redraw(self._win)
        time.sleep(0.05)