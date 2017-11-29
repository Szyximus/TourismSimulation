import pyglet
from agent import Agent


class Simulation():

    def __init__(self):
        self.agent = Agent(100, 100)
        self.agent.velx = 5
        self.agent.vely= 3

    def update(self, dt):
        self.agent.update(dt)

    def draw(self, x, y):
        self.agent.posx = x
        self.agent.posy = y
        self.agent.draw()
