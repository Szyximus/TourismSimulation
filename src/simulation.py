import pyglet
from agent import Agent


class Simulation:

    def __init__(self):
        self.agent = Agent(-438, 600)
        self.agent.velx = -1
        self.agent.vely= 9

    def update(self, dt):
        self.agent.update(dt)

    def draw(self, windowx, windowy):
        self.agent.draw(windowx, windowy)
