import numpy as np
from PIL import Image


class Heatmap:

    def __init__(self, width, height):
        self.image = Image.new('I', (width, height), 0)

   # def update (self, agents):
    #    image = image +100

    def draw(self):
        self.image.show()

