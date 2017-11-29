import pyglet


class Label:
    def __init__(self, window_width):
        self.watermark = 'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek'
        self.label = pyglet.text.Label(
            self.watermark, font_name='Verdana',
            font_size=8, x=window_width - 8,
            y=4, anchor_x='right', anchor_y='bottom')

        self.labelShadow = pyglet.text.Label(
            self.watermark, font_name='Verdana',
            font_size=8, x=window_width - 7, color=(0, 0, 0, 128),
            y=3, anchor_x='right', anchor_y='bottom')

    def draw(self,window_width):
        self.label = pyglet.text.Label(
            self.watermark, font_name='Verdana',
            font_size=8, x=window_width - 8,
            y=4, anchor_x='right', anchor_y='bottom')

        self.labelShadow = pyglet.text.Label(
            self.watermark, font_name='Verdana',
            font_size=8, x=window_width - 7, color=(0, 0, 0, 128),
            y=3, anchor_x='right', anchor_y='bottom')
        self.labelShadow.draw()
        self.label.draw()
