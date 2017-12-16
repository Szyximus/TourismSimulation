import pyglet
from agent import Agent
from spawn_point import SpawnPoint
from point_of_interest import PointOfInterest
from timebox import Timebox

from math import floor
import numpy as np
from PIL import Image


class Simulation:
    DEBUG = True

    def __init__(self, size_x, size_y, window_width, window_height):
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
        self.grid = None
        self.prepare_grid()

        # one meter is 1.5 pixels
        self.pixels_per_meter = 1.5

        # time speed multiplier. 2 means that one second in real is two seconds in simulation
        self.time_speed = 4

        # how often (in simulation time) update will take place
        self.time_density = 1
        self.simulation_delta_time = 0
        self.real_time = 0

        # timestamp = 1513426631.0
        timestamp = 0
        self.timebox = Timebox(timestamp, window_width, window_height)

        # how much grid is smaller than map
        # not used, probably won't help efficiency
        self.grid_scale = 1

    def prepare_grid(self):
        krakow_map_gray = Image.open('./graphics/Navigation.png')
        krakow_map_gray = krakow_map_gray.convert('L')
        self.grid = np.array(krakow_map_gray)
        # PIL (0,0) is in upper left corner, pyglet and our map_raster in bottom left corner
        # after np.flip it will be consistent
        self.grid = np.flip(self.grid, 0)

    def get_grid(self, y, x):
        return self.grid[floor(y * self.grid_scale)][floor(x * self.grid_scale)]

    def set_grid(self, y, x, v):
        self.grid[floor(y * self.grid_scale)][floor(x * self.grid_scale)] = v

    def update(self, dt):
        self.simulation_delta_time += dt * self.time_speed
        self.real_time += dt

        if self.simulation_delta_time >= self.time_density:
            if Simulation.DEBUG:
                print("Real time:", round(self.real_time, 2),
                      "  |  Simulation time:", round(self.real_time * self.time_speed, 2),
                      "  |  Time delta: ", round(self.simulation_delta_time, 2))

            list(map(lambda spawn_point: spawn_point.update(self.simulation_delta_time, self), self.spawn_points))
            list(map(lambda agent: agent.update(self.simulation_delta_time), self.agents))
            self.timebox.update(self.simulation_delta_time)
            self.simulation_delta_time = 0

    def draw(self, windowx, windowy):
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
        list(map(lambda spawn: spawn.draw(windowx, windowy), self.spawn_points))
        list(map(lambda poi: poi.draw(windowx, windowy), self.pois))
        self.timebox.draw()
