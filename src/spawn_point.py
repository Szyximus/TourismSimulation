import pyglet
import time
from agent import Agent
from random import randint
from poilabel import PoiLabel


def current_milli_time():
    return int(round(time.time() * 1000))


class SpawnPoint:

    def __init__(self, x, y, name, agents_per_sec):
        self.x = x
        self.y = y
        self.agents_per_sec = agents_per_sec
        self.name = name

        self.last_activation_time = current_milli_time()

        self.img = pyglet.image.load('./graphics/Spawn.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

        self.label = PoiLabel(name, x, y)

        self.counter = int(16.666 / agents_per_sec)
        self.i = self.counter

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.x
        self.sprite.y = windowy + self.y
        self.sprite.draw()
        self.label.draw(self.sprite.x, self.sprite.y)

    def update(self, agents):
        self.i = self.i - 1
        if self.i == 0:
            self.i = self.counter
            agents.append(Agent(self.x, self.y, randint(-10, 10), randint(-10, 10)))
            pass
