from abc import ABC, abstractmethod
from src.path_finding.point import Point


class PathFinderBase(ABC):

    def __init__(self, grid):
        self.grid = grid
        self.marker = 0

    @abstractmethod
    def get_path(self, start_point, end_point):
        pass

    def is_point_walkable(self, point):
        if not self.grid.is_walkable(point.x, point.y):
            return False
        return True

    def is_path_walkable(self, start_point, end_point):
        for x, y in self.__line(start_point.x, start_point.y, end_point.x, end_point.y):
            if not self.is_point_walkable(Point(x, y)):
                return False
        return True

    # https://stackoverflow.com/questions/25837544/get-all-points-of-a-straight-line-in-python
    @staticmethod
    def __line(x1, y1, x2, y2):
        points = []
        is_steep = abs(y2 - y1) > abs(x2 - x1)
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        rev = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            rev = True
        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        error = int(delta_x / 2)
        y = y1
        if y1 < y2:
            y_step = 1
        else:
            y_step = -1
        for x in range(x1, x2 + 1):
            if is_steep:
                points.append((y, x))
            else:
                points.append((x, y))
            error -= delta_y
            if error < 0:
                y += y_step
                error += delta_x
        # Reverse the list if the coordinates were reversed
        if rev:
            points.reverse()
        return points