from src.path_finding.point import Point
import math
from src.path_finding.grid import Grid

# TODO
# what if agent out of path, calculate again?
# what if user not moved (roadblock), calculate again?
# what if poi unreachable, Exception?

class Walkpath:

    def __init__(self, start_point, end_point, grid, path_precision, end_point_range):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid

        self.precision = path_precision
        self.end_point_range = end_point_range  # TODO  modify
        self.walk_queue = []

        self.calculate_walk_queue()

    @staticmethod
    def from_agent(agent, precision):
        return Walkpath(
            Point(agent.posx, agent.posy),
            Point(agent.current_poi.x, agent.current_poi.y),
            agent.grid,
            precision,
            agent.current_poi.range)  # TODO modify

    def get_direction(self, x, y):
        try:
            next_checkpoint = self.update_then_return_next_checkpoint(x, y)
        except Exception:
            return 0, 0

        return next_checkpoint.diff(Point(x, y))\
            .normalized_vector()\
            .to_touple()

    def calculate_walk_queue(self):
        # calculating an queue of points
        # first point in queue is start_point
        # last point is desired poi position
        # between start and end are checkpoints
        # TODO

        # firstly set end_point in reachable point
        self.make_end_point_reachable()

        self.walk_queue.append(self.start_point)
        self.walk_queue.append(self.end_point)
        return

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

        if current_position.distance_from(next_checkpoint) <= self.precision:
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
