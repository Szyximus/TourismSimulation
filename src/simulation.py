import pyglet
from agent import Agent
from spawn_point import SpawnPoint
from point_of_interest import PointOfInterest


class Simulation:

    def __init__(self):
        self.agents = []
        self.spawn_points = [SpawnPoint(-990, 1300, 1)]
        self.pois = [PointOfInterest(-680, 1090, 'McDonalds', 5, 2, 4), PointOfInterest(-480, 990, 'Sukiennice', 7, 0, 2), PointOfInterest(-310, 980, 'Kościół Mariacki', 3, 0, 8)]

    def update(self, dt):
        list(map(lambda spawn_point: spawn_point.update(self.agents), self.spawn_points))
        list(map(lambda agent: agent.update(dt), self.agents))
        #list(map(lambda poi: poi.update(), self.pois))

    def draw(self, windowx, windowy):
        list(map(lambda spawn: spawn.draw(windowx, windowy), self.spawn_points))
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
        list(map(lambda poi: poi.draw(windowx, windowy), self.pois))

