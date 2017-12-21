import numpy as np
from PIL import Image

class Heatmap:


    def __init__(self, width, height):
        self.image = Image.new('I', {width, height}, 0)

    def draw(self, window_width, window_height, x, y):

        self.krakow_map.blit(x, y)
        self.label.draw(window_width)