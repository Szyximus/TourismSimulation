import pyglet
from src.poilabel import PoiLabel


class PointOfInterest:

    def __init__(self, x, y, name, attractiveness, price, people_limit, time_needed, time_open, time_close, poi_type):
        self.x = x
        self.y = y

        self.name = name
        self.attractiveness = attractiveness
        self.price = price
        self.people_limit = people_limit
        self.time_needed = time_needed
        self.time_open = time_open
        self.time_close = time_close
        self.type = poi_type

        self.img = pyglet.image.load('./graphics/POI.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

        self.label = PoiLabel(name, x, y)

    @classmethod
    def from_dict(cls, name, attributes):
        required_all = ["x", "y", "attractiveness", "price", "time_needed", "poi_type"]
        for required in required_all:
            if required not in attributes.keys():
                raise ValueError("Required key in pois config file not found: {}".format(required))

        if name == "" or name is None:
            raise ValueError("Name can't be empty")
        attributes["name"] = name
        
        return PointOfInterest(**attributes)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.x
        self.sprite.y = windowy + self.y
        self.sprite.draw()
        self.label.draw(self.sprite.x, self.sprite.y)









