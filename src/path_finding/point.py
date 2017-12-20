import math
import pyglet


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # TODO debug cases
        self.sprite_inited = False


    def __str__(self):
        return "x:" + str(self.x) + " y:" + str(self.y)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y)

    def init_sprite(self):
        self.point_img = pyglet.image.load('../graphics/Pin2.png')
        self.sprite = pyglet.sprite.Sprite(self.point_img, x=self.x, y=self.y)
        self.sprite_inited = True

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

    def draw(self, winx, winy):
        if not self.sprite_inited:
            self.init_sprite()
        # TODO debug cases
        self.sprite.x = winx + self.x
        self.sprite.y = winy + self.y
        self.sprite.draw()
