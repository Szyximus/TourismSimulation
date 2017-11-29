import pyglet


class PointOfInterest:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.img = pyglet.image.load('./graphics/POI.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.x
        self.sprite.y = windowy + self.y
        self.sprite.draw()
