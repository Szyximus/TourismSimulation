import unittest
import math
import numpy as np
from src.path_finding.walkpath import *


class WalkpathTest(unittest.TestCase):

    # TODO fix tests

    def test_get_proper_direction(self):
        # given
        grid = np.full((20, 20), 255)
        start_point = Point(3, 3)
        end_point = Point(4, 5)
        walkpath = Walkpath(start_point, end_point, grid, 10, 10)

        # when
        direction = walkpath.get_direction(3,4)

        # then
        self.assertEqual((1/math.sqrt(2), 1/math.sqrt(2)), direction)

    def test_make_endpoint_reachable(self):
        # given
        accessible_point = Point(6, 11)
        end_point = Point(5, 10)

        grid = np.zeros((20, 20))
        grid[accessible_point.x][accessible_point.y] = 255

        start_point = Point(3, 3)
        walkpath = Walkpath(start_point, end_point, grid, 10, 2)

        # when
        walkpath.make_end_point_reachable()

        # then
        self.assertEqual(walkpath.end_point, accessible_point)


