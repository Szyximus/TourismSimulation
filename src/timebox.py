import pyglet


import datetime


class Timebox:
    def __init__(self, timestamp, x, y):
        self.timestamp = timestamp
        self.x = x
        self.y = y

        self.img = pyglet.image.load('../graphics/timebox.png')
        self.img.anchor_x = 0
        self.img.anchor_y = 0
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x-self.img.width, y=self.y-self.img.height)

        self.label = TimeboxLabel(self.to_string(), self.x-self.img.width+30, self.y-self.img.height+45)

    def to_string(self):
        return datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def update(self, dt):
        self.timestamp += dt

    def draw(self):
        self.sprite.draw()
        self.label.draw(self.to_string())


class TimeboxLabel:
    def __init__(self, datetime_str, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

        self.label = pyglet.text.Label(
            datetime_str, color=(0, 0, 0, 255),
            font_name='Calibri', font_size=12,
            x=position_x+7, y=position_y,
            anchor_x='left', anchor_y='top')

        self.labelShadow = pyglet.text.Label(
            datetime_str, font_name='Calibri',
            font_size=9, x=position_x + 8, color=(255, 255, 255, 255),
            y=position_y - 1, anchor_x='left', anchor_y='top')

    def draw(self, datetime_str):
        self.label = pyglet.text.Label(
            datetime_str, color=(0, 0, 0, 255),
            font_name='Calibri', font_size=12,
            x=self.position_x+7, y=self.position_y,
            anchor_x='left', anchor_y='top')

        self.labelShadow = pyglet.text.Label(
            datetime_str, font_name='Calibri',
            font_size=9, x=self.position_x + 8, color=(255, 255, 255, 255),
            y=self.position_y - 1, anchor_x='left', anchor_y='top')

        self.labelShadow.draw()
        self.label.draw()
