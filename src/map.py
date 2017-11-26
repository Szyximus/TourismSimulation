import pyglet

watermark = 'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek'

class Map:

    def __init__(self, window_width, window_height):
        self.krakow_map = pyglet.image.load('./src/graphics/Krk.png')
        self.krakow_map.anchor_x = self.krakow_map.width // 2
        self.krakow_map.anchor_y = self.krakow_map.height // 2

        self.label = pyglet.text.Label(
            watermark, font_name='Verdana',
            font_size=8, x=window_width - 8,
            y=4, anchor_x='right', anchor_y='bottom')

        self.labelShadow = pyglet.text.Label(
            watermark, font_name='Verdana',
            font_size=8, x=window_width - 7, color=(0, 0, 0, 128),
            y=3, anchor_x='right', anchor_y='bottom')

    def draw(self, window_width, window_height, x, y):

        self.krakow_map.blit(x, y)

        self.labelShadow.draw()
        self.label.draw()
