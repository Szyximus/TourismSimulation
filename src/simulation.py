import pyglet
from agent import Agent
from spawn_point import SpawnPoint


class Simulation:

    def __init__(self):
        self.agents = []
        self.spawn_points = [SpawnPoint(0, 0, 1)]

    def update(self, dt):
        list(map(lambda spawn_point: spawn_point.update(self.agents), self.spawn_points))
        list(map(lambda agent: agent.update(dt), self.agents))

    def draw(self, windowx, windowy):
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
