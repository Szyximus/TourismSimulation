import unittest
import math
import numpy as np
from src.path_finding import *


class WalkpathTest(unittest.TestCase):

    def test_get_proper_direction(self):
        # given
        grid = self.walkable_grid()
        start_point = Point(3, 3)
        end_point = Point(4, 5)
        walkpath = Walkpath(start_point, end_point, grid, 10, 10)

        # when
        direction = walkpath.get_direction(3,4)

        # then
        self.assertEqual((1/math.sqrt(2), 1/math.sqrt(2)), direction)

    def test_make_endpoint_reachable(self):
        # given
        accessible_point = Point(2, 4)
        end_point = Point(1, 2)
        end_point_range = 3

        grid = self.unwalkable_grid()
        grid.set_walkability(accessible_point.x, accessible_point.y, True)

        start_point = Point(3, 3)
        walkpath = Walkpath(start_point, end_point, grid, end_point_range)

        # when
        walkpath.make_end_point_reachable()

        # then
        self.assertEqual(walkpath.end_point, accessible_point)

    def test_is_path_walkable_on_fully_walkable_grid(self):
        # given
        start_point = Point(-4, -9)
        end_point = Point(9, 9)

        grid = self.walkable_grid()
        walkpath = Walkpath(start_point, end_point, grid, 10, 1)

        # when
        actual_result = walkpath.__is_path_walkable(start_point, end_point)

        # exp
        self.assertEqual(actual_result, True)

    def test_is_path_walkable_on_fully_unwalkable_grid(self):
        # given
        start_point = Point(-4, -9)
        end_point = Point(9, 9)

        grid = self.unwalkable_grid()
        grid.set_walkability(9, 9, True)
        walkpath = Walkpath(start_point, end_point, grid, 10, 1)

        # when
        actual_result = walkpath.is_path_walkable(start_point, end_point)

        # exp
        self.assertEqual(actual_result, False)

    def test_is_path_walkable_on_specific_walkable_path_grid(self):
        # given
        start_point = Point(1, -2)
        end_point = Point(1, 2)

        grid = self.unwalkable_grid()
        grid.set_walkability(1, -2, True)
        grid.set_walkability(1, -1, True)
        grid.set_walkability(1, 0, True)
        grid.set_walkability(1, 1, True)
        grid.set_walkability(1, 2, True)
        walkpath = Walkpath(start_point, end_point, grid, 1, 1)

        # when
        actual_result = walkpath.is_path_walkable(start_point, end_point)

        # exp
        self.assertEqual(actual_result, True)

    def test_is_path_walkable_on_specific_walkable_path_grid2(self):
        # given
        start_point = Point(-2, -2)
        end_point = Point(2, 2)

        grid = self.unwalkable_grid()
        grid.set_walkability(-2, -2, True)
        grid.set_walkability(-1, -1, True)
        grid.set_walkability(0, 0, True)
        grid.set_walkability(1, 1, True)
        grid.set_walkability(2, 2, True)
        walkpath = Walkpath(start_point, end_point, grid, 1, 1)

        # when
        actual_result = walkpath.is_path_walkable(start_point, end_point)

        # exp
        self.assertEqual(actual_result, True)

    @staticmethod
    def unwalkable_grid():
        return Grid(np.zeros((20, 20)), 20, 20)

    @staticmethod
    def walkable_grid():
        return Grid(np.full((20,20), 255), 20, 20)