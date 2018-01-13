import pyglet
from label import Label;

watermark = 'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek'


class Map:

    def __init__(self, window_width, window_height):
        self.krakow_map = pyglet.image.load('./graphics/Krk.png')
        self.krakow_map.anchor_x = self.krakow_map.width // 2
        self.krakow_map.anchor_y = self.krakow_map.height // 2
        self.label = Label(window_width)

    def draw(self, window_width, window_height, x, y):

        self.krakow_map.blit(x, y)
        self.label.draw(window_width)
