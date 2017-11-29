import pyglet


class PoiLabel:
    def __init__(self, name, position_x, position_y):
        self.name = name
        self.label = pyglet.text.Label(
            self.name, font_name='Calibri',
            font_size=8, x=position_x+7,
            y=position_y, anchor_x='left', anchor_y='top')

        self.labelShadow = pyglet.text.Label(
            self.name, font_name='Calibri',
            font_size=8, x=position_x + 8, color=(0, 0, 0, 128),
            y=position_y - 1, anchor_x='left', anchor_y='top')

    def draw(self, position_x, position_y):
        self.label = pyglet.text.Label(
            self.name, font_name='Calibri',
            font_size=8, x=position_x + 7,
            y=position_y, anchor_x='left', anchor_y='top')

        self.labelShadow = pyglet.text.Label(
            self.name, font_name='Calibri',
            font_size=8, x=position_x + 8, color=(0, 0, 0, 128),
            y=position_y - 1, anchor_x='left', anchor_y='top')
        self.labelShadow.draw()
        self.label.draw()