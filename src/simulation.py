import pyglet
from agent import Agent
from spawn_point import SpawnPoint
from point_of_interest import PointOfInterest

import numpy as np
from PIL import Image


class Simulation:

    def __init__(self, size_x, size_y):
        self.agents = []
        self.spawn_points = [SpawnPoint(-990, 1300, 'Teatr Bagatela', 1),
                             SpawnPoint(-900, 540, 'Filharmonia', 0.2),
                             SpawnPoint(-430, 555, 'Plac Wszystkich Świętych', 0.5),
                             SpawnPoint(35, 625, 'Poczta Główna', 0.8),
                             SpawnPoint(350, 1450, 'Dworzec Główny', 0.5),
                             SpawnPoint(-270, 1750, 'Stary Kleparz', 0.2)]

        self.pois = [PointOfInterest(-660, 1077, 'McDonald\'s', 5, 2, 4, None),
                     PointOfInterest(-480, 990, 'Sukiennice', 7, 0, 2, None),
                     PointOfInterest(-571, 1125, 'Polonia Wax Museum', 2, 8, 5, None),
                     PointOfInterest(-540, 1195, 'Bobby Burger', 6, 5, 4, None),
                     PointOfInterest(-315, 982, 'Bazylika Mariacka', 3, 0, 8, None),
                     PointOfInterest(-410, 955, 'Pomnik Adama Mickiewicza', 2, 0, 1, None),
                     PointOfInterest(-315, 1075, 'Pijalnia Czekolady E. Wedel', 6, 7, 6, None),
                     PointOfInterest(-440, 851, 'Kościół Świętego Wojciecha', 2, 0, 5, None),
                     PointOfInterest(-585, 955, 'Wieża Ratuszowa', 2, 1, 3, None)]

        self.size_x, self.size_y = size_x, size_y
        self.map_raster = None
        self.prepare_map_raster()

        self.pixels_per_meter = 1.5

    def prepare_map_raster(self):
        krakow_map_gray = Image.open('./graphics/Navigation.png')
        krakow_map_gray = krakow_map_gray.convert('L')
        self.map_raster = np.flip(np.array(krakow_map_gray), 0)
        # PIL (0,0) is in upper left corner, pyglet and our map_raster in bottom left corner
        # after np.flip it will be consistent

    def update(self, dt):
        list(map(lambda spawn_point: spawn_point.update(self.agents, self), self.spawn_points))
        list(map(lambda agent: agent.update(dt), self.agents))

    def draw(self, windowx, windowy):
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
        list(map(lambda spawn: spawn.draw(windowx, windowy), self.spawn_points))
        list(map(lambda poi: poi.draw(windowx, windowy), self.pois))

