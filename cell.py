from graphics import Line, Point

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall == True:
            left_wall = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_wall)
        if self.has_right_wall == True:
            right_wall = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_wall)
        if self.has_top_wall == True:
            top_wall = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_wall)
        if self.has_bottom_wall == True:
            bottom_wall = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_wall)
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        self_middle = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        to_cell_middle = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        if undo != True:
            fill_color = "red"
        else:
            fill_color = "gray"
        move = Line(self_middle, to_cell_middle)
        self._win.draw_line(move, fill_color)
            