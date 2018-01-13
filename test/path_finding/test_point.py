import unittest
from src.path_finding.walkpath import *


class PointTest(unittest.TestCase):

    def test_distance_from(self):
        result = Point(1,2).distance_from(Point(1,1))
        self.assertEqual(result, 1)

    def test_normalized_vector(self):
        vec = Point(1, 1)
        expected_result = Point(1/math.sqrt(2), 1/math.sqrt(2))
        self.assertEqual(expected_result, vec.normalized_vector())