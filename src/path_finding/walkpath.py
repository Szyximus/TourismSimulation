from src.path_finding.point import Point
import math
from src.path_finding.grid import Grid

# TODO
# what if agent out of path, calculate again?
# what if user not moved (roadblock), calculate again?
# what if poi unreachable, Exception?

class Walkpath:

    def __init__(self, start_point, end_point, grid, end_point_range):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid

        self.end_point_range = end_point_range  # TODO  modify
        self.walk_queue = []
        self.precision = 2

        self.calculate_walk_queue()

    @staticmethod
    def from_agent(agent):
        return Walkpath(
            Point(agent.posx, agent.posy),
            Point(agent.current_poi.x, agent.current_poi.y),
            agent.grid,
            agent.current_poi.range)  # TODO modify

    def get_direction(self, x, y, speed):
        try:
            next_checkpoint = self.update_then_return_next_checkpoint(x, y)
        except Exception:
            return 0, 0

        desired_direction = next_checkpoint.diff(Point(x, y)).normalized_vector()

        if not self.is_point_walkable(Point(x, y).add(desired_direction)):
            self.calculate_walk_queue()
            return (0, 0)

        return desired_direction.to_touple()

    def calculate_walk_queue(self):
        self.make_end_point_reachable()
        self.walk_queue = self.path_finding_algorithm(self.end_point, self.start_point)
        return

    def path_finding_algorithm(self, end_point, start_point):
        step = 10
        path_finding_queue = PathFindingQueue(step)
        counter = 0
        path_finding_queue.put(end_point, counter)
        checked_point = path_finding_queue.get_next()[0]
        counter = 1

        while not self.is_path_walkable(start_point, checked_point):

            for x in [-step, 0, step]:
                for y in [-step, 0, step]:

                    examined_point = checked_point.add(Point(x, y))
                    if self.is_path_walkable(checked_point, examined_point):
                        path_finding_queue.put(examined_point, counter)
                        if self.is_path_walkable(examined_point, start_point):
                            return path_finding_queue.get_path()

            next = path_finding_queue.get_next()
            checked_point = next[0]
            counter = next[1] + 1

        return path_finding_queue.get_path()

    def is_path_walkable(self, start_point, end_point):
        for x, y in line(start_point.x, start_point.y, end_point.x, end_point.y):
            if not self.is_point_walkable(Point(x, y)):
                return False
        return True

    def is_point_walkable(self, point):
        # for r in range(self.precision):
        #     for theta in range(36):
        #         angle = math.radians(theta * 10)
        #         x = point.x + int(math.ceil(r * math.cos(angle)))
        #         y = point.y + int(math.ceil(r * math.sin(angle)))
        #
        precision = 1
        for x in range(point.x-precision, point.x+precision):
            for y in range(point.y - precision, point.y + precision):
                if not self.grid.is_walkable(x, y):
                        return False
        return True

    def make_end_point_reachable(self):
        # TODO optimize
        for r in range(self.end_point_range):
            for theta in range(360):
                angle = math.radians(theta)
                x = self.end_point.x + int(math.ceil(r * math.cos(angle)))
                y = self.end_point.y + int(math.ceil(r * math.sin(angle)))
                if self.grid.is_walkable(x, y):
                    self.end_point = Point(x, y)
                    return
        raise NotReachableEndPointException(self.end_point)

    def update_then_return_next_checkpoint(self, x, y):
        next_checkpoint = self.get_next_checkpoint()
        current_position = Point(x, y)

        if current_position.distance_from(next_checkpoint) <= 5:
            self.walk_queue.pop(0)
            return self.get_next_checkpoint()

        return next_checkpoint

    def get_next_checkpoint(self):
        if len(self.walk_queue) > 0:
            return self.walk_queue[0]
        else:
            raise NoCheckpointsInQueueException()


class NotReachableEndPointException(Exception):
    def __init__(self, point):
        self.end_point = point
    pass


class NoCheckpointsInQueueException(Exception):
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