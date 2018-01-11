from src.path_finding.path_finders.heavy_path_finder import HeavyPathFinder
from src.path_finding.point import Point
from src.path_finding.path_cache import PathCache, PathNotInCacheException


class Walkpath:

    def __init__(self, start_point, end_point, grid):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = grid
        self.path_finder = HeavyPathFinder(self.grid)

        self.walk_queue = []

        self.__calculate_walk_queue()

    @staticmethod
    def from_agent(agent):
        return Walkpath(
            Point(agent.posx, agent.posy),
            Point(agent.current_poi.x, agent.current_poi.y),
            agent.grid)

    def get_direction(self, x, y):
        try:
            next_checkpoint = self.update_then_return_next_checkpoint(x, y)
        except Exception:
            return 0, 0

        desired_direction = next_checkpoint.diff(Point(x, y)).normalized_vector()

        return desired_direction.to_touple()

    def draw(self, winx, winy):
        list(map(lambda point: point.draw(winx, winy), self.walk_queue))

    def __calculate_walk_queue(self):
        try:
            self.walk_queue = PathCache().get(self.start_point, self.end_point)
        except PathNotInCacheException:
            try:
                self.walk_queue = self.path_finder.get_path(self.start_point, self.end_point)
            except:
                print('ERROR: Not able to generate walkpath from {} to {}'.format(self.start_point, self.end_point))
                self.walk_queue = [self.end_point]
            PathCache().put(self.start_point, self.end_point, self.walk_queue)
        return

    def update_then_return_next_checkpoint(self, x, y):
        next_checkpoint = self.get_next_checkpoint()
        current_position = Point(x, y)

        # TODO hardcoded precision, may be moved to configs
        if current_position.distance_from(next_checkpoint) <= 5:
            self.walk_queue.pop(0)
            return self.get_next_checkpoint()

        return next_checkpoint

    def get_next_checkpoint(self):
        if len(self.walk_queue) > 0:
            return self.walk_queue[0]
        else:
            raise NoCheckpointsInQueueException()


class NoCheckpointsInQueueException(Exception):
    pass
