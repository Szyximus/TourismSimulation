from src.path_finding.point import Point
import math
import random
from src.path_finding.path_finder import PathFinder
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
        self.path_finder = PathFinder(self.grid)

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

        expected_position = Point(x, y).add(desired_direction).to_touple()
        if not self.grid.is_walkable(expected_position[0], expected_position[1]):
            return random.uniform(0.0,1.0), random.uniform(0.0,1.0)

        return desired_direction.to_touple()

    def draw(self, winx, winy):
        list(map(lambda point: point.draw(winx, winy), self.walk_queue))

    def calculate_walk_queue(self):
        self.make_end_point_reachable()
        self.walk_queue = self.path_finder.get_path(self.start_point, self.end_point)
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