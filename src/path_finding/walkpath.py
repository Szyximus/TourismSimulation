import random

from src.path_finding.path_finders.heavy_path_finder import HeavyPathFinder
from src.path_finding.point import Point


class Walkpath:

    def __init__(self, start_point, end_point, grid, end_point_range):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid
        self.path_finder = HeavyPathFinder(self.grid)
        self.end_point_range = end_point_range

        self.walk_queue = []

        self.__calculate_walk_queue()

    @staticmethod
    def from_agent(agent):
        return Walkpath(
            Point(agent.posx, agent.posy),
            Point(agent.current_poi.x, agent.current_poi.y),
            agent.grid,
            agent.current_poi.range)

    def get_direction(self, x, y):
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

    def __calculate_walk_queue(self):
        self.__make_end_point_reachable()
        self.walk_queue = self.path_finder.get_path(self.start_point, self.end_point)
        return

    def __make_end_point_reachable(self):
        for x in range(self.end_point_range + 1):
            for y in range(self.end_point_range + 1):
                checked = self.end_point.add(Point(x, y))
                walkable = self.grid.is_walkable(checked.x, checked.y)
                distance_from = self.end_point.distance_from(checked)
                if walkable & (distance_from <= self.end_point_range):
                    self.end_point = checked
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
