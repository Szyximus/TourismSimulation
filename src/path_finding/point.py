import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:" + str(self.x) + " y:" + str(self.y)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def distance_from(self, point):
        return math.sqrt(abs(self.x - point.x) ** 2 + abs(self.y - point.y) ** 2)

    def normalized_vector(self):
        length = self.distance_from(Point(0, 0))
        if length == 0:
            return Point(0, 0)
        return Point(self.x/length, self.y/length)

    def diff(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def to_touple(self):
        return self.x, self.y