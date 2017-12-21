import pyglet
from agent import Agent
from spawn_point import SpawnPoint
from point_of_interest import PointOfInterest
from heatmap import Heatmap
import numpy as np
import yaml

from PIL import Image


class Simulation:

    def __init__(self, size_x, size_y, config_file):
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
        self.map_raster = None
        self.prepare_map_raster()

        self.pixels_per_meter = 1.5

        self.heatmap = Heatmap(size_x, size_y)

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
        self.heatmap.update(self.agents)
