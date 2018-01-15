from src.spawn_point import SpawnPoint
from src.point_of_interest import PointOfInterest
from src.timebox import Timebox

from math import floor
import pyglet
from src.agent import Agent
from src.spawn_point import SpawnPoint
from src.point_of_interest import PointOfInterest
from src.heatmap import Heatmap
import numpy as np
import yaml
import datetime
import time

from PIL import Image


class Simulation:
    DEBUG = True

    def __init__(self, size_x, size_y, window_width, window_height, config_file):
        try:
            with open(config_file, 'r') as config:
                config =  yaml.safe_load(config)
        except FileNotFoundError as e:
            raise FileNotFoundError("Config file not found")
        except yaml.YAMLError as e:
            raise yaml.YAMLError("Config file error: {}".format(e))

        if any(required not in config.keys() for required in ("pois_file", "spawn_points_file")):
            raise ValueError("Required keys in config file not found")

        with open(config["spawn_points_file"], 'r') as spawn_points:
            spawn_points = yaml.safe_load(spawn_points)
        self.spawn_points = [SpawnPoint.from_dict(sp_name, spawn_points[sp_name]) for sp_name in spawn_points.keys()]

        with open(config["pois_file"], 'r') as pois:
            pois = yaml.safe_load(pois)
        self.pois = [PointOfInterest.from_dict(poi_name, pois[poi_name]) for poi_name in pois.keys()]

        self.agents = []


        self.size_x, self.size_y = size_x, size_y
        self.grid = None
        self.prepare_grid()

        # one meter is 1.5 pixels
        self.pixels_per_meter = 1.5

        # time speed multiplier. 2 means that one second in real is two seconds in simulation
        self.time_speed = int(config['speed_multiplier'])
        ## TODO: Walking is bugged if time_speed > 3

        # how often (in simulation time) update will take place
        self.time_density = 1.0 / self.time_speed
        self.simulation_delta_time = 0
        self.real_time = 0

        # timestamp = 1516298340
        timestamp = int(time.mktime(time.strptime('18/01/2018 ' + config['start_time'], "%d/%m/%Y %H:%M")))
        self.timebox = Timebox(timestamp, window_width, window_height)

        # how much grid is smaller than map
        # not used, probably won't help efficiency
        self.grid_scale = 1

        self.heatmap = Heatmap(size_x, size_y)

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

        self.heatmap.update(self.agents, self.timebox.timestamp)

    def draw(self, windowx, windowy, window_width, window_height):
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
        list(map(lambda spawn: spawn.draw(windowx, windowy), self.spawn_points))
        list(map(lambda poi: poi.draw(windowx, windowy), self.pois))
        self.timebox.draw(window_width, window_height)

