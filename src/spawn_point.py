import pyglet
import time
from agent import Agent
from random import randint


def current_milli_time():
    return int(round(time.time() * 1000))


class SpawnPoint:

    def __init__(self, x, y, agents_per_sec):
        self.x = x
        self.y = y
        self.agents_per_sec = agents_per_sec

        self.last_activation_time = current_milli_time()

        self.img = pyglet.image.load('./graphics/Spawn.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.x
        self.sprite.y = windowy + self.y
        self.sprite.draw()

    def update(self, agents):
        agents.append(Agent(self.x, self.y, randint(-1, 8), randint(-6, 1)))