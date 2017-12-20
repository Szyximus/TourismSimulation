from src.path_finding.point import Point
import math

class PathFinder:

    def __init__(self, grid):
        self.grid = grid
        pass

    def get_path(self, start_point, end_point):
        step = 5
        directions = 8

        path_finding_queue = PathFindingQueue(step)
        counter = 0
        path_finding_queue.put(end_point, counter)
        checked_point = path_finding_queue.get_next()[0]
        counter = 1

        while start_point.distance_from(checked_point) > 4 * step & (not self.is_path_walkable(start_point, checked_point)):

            print("Checking point " + str(checked_point))

            vectors = []
            for dire in range(0, directions):
                vectors.append(
                    Point.from_polar_coordinates(step, dire/directions * 2 * math.pi).round())

            while len(vectors) > 0:
                vector = vectors.pop()
                examined_point = checked_point.add(Point(round(vector.x), round(vector.y)))
                # if self.is_path_walkable(checked_point, examined_point):
                if self.is_point_walkable(examined_point):
                    path_finding_queue.put(examined_point, counter)
                    # if start_point.distance_from(examined_point) < step: #& self.is_path_walkable(examined_point, start_point):
                    #     return path_finding_queue.get_path()

            next_point = path_finding_queue.get_next()
            checked_point = next_point[0]
            counter = next_point[1] + 1

        return path_finding_queue.get_path()

    def is_point_walkable(self, point):
        if not self.grid.is_walkable(point.x, point.y):
            return False
        return True

    def is_path_walkable(self, start_point, end_point):
        for x, y in line(start_point.x, start_point.y, end_point.x, end_point.y):
            if not self.is_point_walkable(Point(x, y)):
                return False
        return True


class PathFindingQueue:

    def __init__(self, step):
        self.points_queue = []
        self.counter_queue = []
        self.current_index = 0
        self.step = step

    def put(self, point, counter):
        try:
            self.points_queue.index(point)
        except:
            self.points_queue.append(point)
            self.counter_queue.append(counter)

    def get_next(self):
        try:
            result = self.points_queue[self.current_index], self.counter_queue[self.current_index]
            self.current_index = self.current_index + 1
            return result
        except:
            raise EndPointUnreachableException()

    def get_path(self):
        # TODO refactoring
        index = len(self.points_queue) - 1
        last_point = self.points_queue[index]
        points = [last_point]
        current_counter = self.counter_queue[index] - 1

        while index > 0:
            index = index - 1
            abs1 = abs(last_point.x - self.points_queue[index].x)
            abs2 = abs(last_point.y - self.points_queue[index].y)
            counter = self.counter_queue[index]
            if (counter == current_counter) & (abs1 <= self.step) & (abs2 <= self.step):
                    last_point = self.points_queue[index]
                    points.insert(0, last_point)
                    current_counter = current_counter - 1

        points.reverse()
        return points


class EndPointUnreachableException(Exception):
    pass

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