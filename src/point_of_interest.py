import pyglet
from src.poilabel import PoiLabel


class PointOfInterest:

    def __init__(self, x, y, name, attractiveness, price, time_needed, type):
        self.x = x
        self.y = y

        self.name = name
        self.attractiveness = attractiveness
        self.price = price
        self.time_needed = time_needed
        self.type = type

        self.img = pyglet.image.load('../graphics/POI.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

        self.label = PoiLabel(name, x, y)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.x
        self.sprite.y = windowy + self.y
        self.sprite.draw()
        self.label.draw(self.sprite.x, self.sprite.y)









