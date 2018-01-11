import pyglet
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # debug cases
        self.sprite_inited = False

    @staticmethod
    def from_polar_coordinates(r, theta_radians):
        x = r * math.cos(theta_radians)
        y = r * math.sin(theta_radians)
        return Point(x, y)

    def init_sprite(self):
        self.point_img = pyglet.image.load('../graphics/Pin2.png')
        self.sprite = pyglet.sprite.Sprite(self.point_img, x=self.x, y=self.y)
        self.sprite_inited = True

    def __str__(self):
        return "x:" + str(self.x) + " y:" + str(self.y)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def __hash__(self) -> int:
        return int(self.x + self.y)

    def distance_from(self, point):
        return math.sqrt(abs(self.x - point.x) ** 2 + abs(self.y - point.y) ** 2)

    def normalized_vector(self):
        length = self.distance_from(Point(0, 0))
        if length == 0:
            return Point(0, 0)
        return Point(self.x/length, self.y/length)

    def diff(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def add(self, direction):
        return Point(round(self.x + direction.x), round(self.y + direction.y))

    def to_touple(self):
        return self.x, self.y

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        return self

    def draw(self, winx, winy):
        if not self.sprite_inited:
            self.init_sprite()
        # debug cases
        self.sprite.x = winx + self.x
        self.sprite.y = winy + self.y
        self.sprite.draw()