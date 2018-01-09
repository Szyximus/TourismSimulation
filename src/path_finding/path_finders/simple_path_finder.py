from src.path_finding.path_finders.path_finder_base import PathFinderBase


# TODO
class SimplePathFinder(PathFinderBase):

    def __init__(self, grid):
        super().__init__(grid)
        self.grid = grid

    def get_path(self, start_point, end_point):
        pass


