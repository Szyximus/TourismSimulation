from src.path_finding.point import Point
import random
from src.path_finding.path_finders.path_finder_base import PathFinderBase


class HeavyPathFinder(PathFinderBase):

    def __init__(self, grid):
        super().__init__(grid)

        # algorithm parameters
        self.step = 5

    def get_path(self, start_point, end_point):
        path_finding_queue = PathFindingQueue(self.step)
        counter = 0
        path_finding_queue.put(end_point, counter)
        checked_point = path_finding_queue.get_next()[0]
        counter = 1

        while start_point.distance_from(checked_point) > self.step:

            points_to_examine = [checked_point.add(Point(0, self.step)),
                                 checked_point.add(Point(0, -self.step)),
                                 checked_point.add(Point(self.step, 0)),
                                 checked_point.add(Point(-self.step, 0))]

            for point in points_to_examine:
                if self.is_path_walkable(checked_point, point):
                    path_finding_queue.put(point, counter)
                    if start_point.distance_from(point) <= self.step:
                        return path_finding_queue.get_path()

            next_point = path_finding_queue.get_next()
            checked_point = next_point[0]
            counter = next_point[1] + 1

        path = path_finding_queue.get_path()
        return path


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
        index = len(self.points_queue) -1
        last_point = self.points_queue[index]
        points = [last_point]
        current_counter = self.counter_queue[index] - 1

        same_level_points = []

        while index > 0:
            index = index - 1
            abs1 = abs(last_point.x - self.points_queue[index].x)
            abs2 = abs(last_point.y - self.points_queue[index].y)
            counter = self.counter_queue[index]
            if (counter == current_counter) & (abs1 <= self.step) & (abs2 <= self.step):
                last_point = self.points_queue[index]
                points.insert(0, last_point)
                current_counter = current_counter - 1
            if counter < current_counter:
                rand_index = int(random.uniform(0, len(same_level_points)))
                last_point = same_level_points[rand_index]
                same_level_points = [self.points_queue[index]]
                current_counter = current_counter - 1

        points.reverse()
        return self.__pop_every_second(points)

    @staticmethod
    def __pop_every_second(list_):
        i = 1
        while i < len(list_):
            list_.pop(i)
            i += 1
        return list_


class EndPointUnreachableException(Exception):
    pass


class StartPointNotWalkableException(Exception):
    pass
