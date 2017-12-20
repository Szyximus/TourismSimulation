from src.path_finding.point import Point
import math

class SimplePathFinder:

    def __init__(self, grid):
        self.grid = grid

    def get_path(self, start_point, end_point):
        pass

    def is_point_walkable(self, point):
        if not self.grid.is_walkable(point.x, point.y):
            return False
        return True

    def is_path_walkable(self, start_point, end_point):
        for x, y in line(start_point.x, start_point.y, end_point.x, end_point.y):
            if not self.is_point_walkable(Point(x, y)):
                return False
        return True


# https://stackoverflow.com/questions/25837544/get-all-points-of-a-straight-line-in-python
def line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points
