import numpy as np
from PIL import Image
from PIL import ImageFilter
import datetime


class Heatmap:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = np.zeros((height, width))
        self.image = Image.fromarray(self.array, 'L')
        self.krakow_map = Image.open('./graphics/Krk.png')
        self.timer = 20



    def update (self, agents, timestamp):
        for agent in agents:
            x = agent.posx + (self.width // 2)
            y = (agent.posy - (self.height // 2)) * -1

            #Pseudo Gaussian to prettify

            self.array[y + 2][x - 2] += 1
            self.array[y + 2][x - 1] += 4
            self.array[y + 2][x] += 6
            self.array[y + 2][x + 1] += 4
            self.array[y + 2][x + 2] += 1

            self.array[y + 1][x - 2] += 4
            self.array[y + 1][x - 1] += 16
            self.array[y + 1][x] += 20
            self.array[y + 1][x + 1] += 16
            self.array[y][x + 2] += 4

            self.array[y][x - 2] += 6
            self.array[y][x - 1] += 20
            self.array[y][x] += 24
            self.array[y][x + 1] += 20
            self.array[y][x + 2] += 6

            self.array[y - 2][x - 2] += 4
            self.array[y - 1][x - 1] += 16
            self.array[y][x] += 20
            self.array[y + 1][x + 1] += 16
            self.array[y + 2][x + 2] += 4

            self.array[y - 2][x - 2] += 1
            self.array[y - 2][x - 1] += 4
            self.array[y - 2][x] += 6
            self.array[y - 2][x + 1] += 4
            self.array[y - 2][x + 2] += 1

        if self.timer > 0:
            self.timer -= 1

        # Print at 18:00, 19:00 etc, timer prevents from printing to many maps
        if  int(datetime.datetime.fromtimestamp(timestamp).minute) <= 2:
            if self.timer <= 0:
                self.draw(timestamp)
                self.timer = 20

    def draw(self, timestamp):
        self.image = Image.fromarray(np.uint8(self.array)).filter(ImageFilter.GaussianBlur(radius=7))
        self.image = Image.eval(self.image, lambda px: px * 2 if px * 2 <= 255 else 255 )
        # LUT table for coloring:
        self.image.putpalette([
            0, 0, 128,
            0, 0, 144,
            0, 0, 150,
            0, 0, 166,
            0, 0, 182,
            0, 0, 194,
            0, 0, 216,
            0, 0, 255,
            0, 4, 255,
            0, 8, 255,
            0, 12, 255,
            0, 16, 255,
            0, 20, 255,
            0, 24, 255,
            0, 28, 255,
            0, 32, 255,
            0, 36, 255,
            0, 40, 255,
            0, 44, 255,
            0, 48, 255,
            0, 52, 255,
            0, 56, 255,
            0, 60, 255,
            0, 64, 255,
            0, 68, 255,
            0, 72, 255,
            0, 76, 255,
            0, 80, 255,
            0, 84, 255,
            0, 88, 255,
            0, 92, 255,
            0, 96, 255,
            0, 100, 255,
            0, 104, 255,
            0, 108, 255,
            0, 112, 255,
            0, 116, 255,
            0, 120, 255,
            0, 124, 255,
            0, 128, 255,
            0, 132, 255,
            0, 136, 255,
            0, 140, 255,
            0, 144, 255,
            0, 148, 255,
            0, 152, 255,
            0, 156, 255,
            0, 160, 255,
            0, 164, 255,
            0, 168, 255,
            0, 172, 255,
            0, 176, 255,
            0, 180, 255,
            0, 194, 255,
            0, 198, 255,
            0, 202, 255,
            0, 206, 255,
            0, 210, 255,
            0, 214, 255,
            0, 218, 255,
            0, 222, 255,
            0, 226, 255,
            0, 230, 255,
            0, 234, 255,
            0, 238, 255,
            0, 242, 255,
            0, 248, 255,
            0, 251, 255,
            0, 255, 254,
            0, 255, 250,
            0, 255, 246,
            0, 255, 242,
            0, 255, 238,
            0, 255, 234,
            0, 255, 230,
            0, 255, 226,
            0, 255, 222,
            0, 255, 218,
            0, 255, 214,
            0, 255, 210,
            0, 255, 206,
            0, 255, 202,
            0, 255, 198,
            0, 255, 194,
            0, 255, 190,
            0, 255, 186,
            0, 255, 182,
            0, 255, 178,
            0, 255, 174,
            0, 255, 170,
            0, 255, 166,
            0, 255, 162,
            0, 255, 158,
            0, 255, 154,
            0, 255, 150,
            0, 255, 146,
            0, 255, 142,
            0, 255, 138,
            0, 255, 134,
            0, 255, 130,
            0, 255, 126,
            0, 255, 122,
            0, 255, 118,
            0, 255, 114,
            0, 255, 110,
            0, 255, 106,
            0, 255, 102,
            0, 255, 98,
            0, 255, 94,
            0, 255, 90,
            0, 255, 86,
            0, 255, 82,
            0, 255, 78,
            0, 255, 74,
            0, 255, 70,
            0, 255, 66,
            0, 255, 62,
            0, 255, 48,
            0, 255, 44,
            0, 255, 40,
            0, 255, 36,
            0, 255, 32,
            0, 255, 28,
            0, 255, 24,
            0, 255, 18,
            0, 255, 16,
            0, 255, 12,
            0, 255, 8,
            0, 255, 4,
            4, 255, 0,
            6, 255, 0,
            10, 255, 0,
            16, 255, 0,
            20, 255, 0,
            24, 255, 0,
            28, 255, 0,
            32, 255, 0,
            36, 255, 0,
            40, 255, 0,
            44, 255, 0,
            48, 255, 0,
            52, 255, 0,
            56, 255, 0,
            60, 255, 0,
            64, 255, 0,
            68, 255, 0,
            72, 255, 0,
            76, 255, 0,
            80, 255, 0,
            84, 255, 0,
            88, 255, 0,
            92, 255, 0,
            96, 255, 0,
            100, 255, 0,
            104, 255, 0,
            108, 255, 0,
            112, 255, 0,
            116, 255, 0,
            120, 255, 0,
            124, 255, 0,
            128, 255, 0,
            132, 255, 0,
            136, 255, 0,
            140, 255, 0,
            144, 255, 0,
            148, 255, 0,
            152, 255, 0,
            156, 255, 0,
            160, 255, 0,
            164, 255, 0,
            168, 255, 0,
            172, 255, 0,
            176, 255, 0,
            180, 255, 0,
            184, 255, 0,
            188, 255, 0,
            192, 255, 0,
            196, 255, 0,
            200, 255, 0,
            204, 255, 0,
            208, 255, 0,
            212, 255, 0,
            216, 255, 0,
            220, 255, 0,
            224, 255, 0,
            228, 255, 0,
            232, 255, 0,
            236, 255, 0,
            240, 255, 0,
            244, 255, 0,
            248, 255, 0,
            252, 255, 0,
            255, 255, 0,
            255, 252, 0,
            255, 248, 0,
            255, 244, 0,
            255, 240, 0,
            255, 236, 0,
            255, 232, 0,
            255, 228, 0,
            255, 224, 0,
            255, 220, 0,
            255, 216, 0,
            255, 212, 0,
            255, 208, 0,
            255, 204, 0,
            255, 200, 0,
            255, 196, 0,
            255, 192, 0,
            255, 188, 0,
            255, 184, 0,
            255, 180, 0,
            255, 176, 0,
            255, 172, 0,
            255, 168, 0,
            255, 164, 0,
            255, 160, 0,
            255, 156, 0,
            255, 152, 0,
            255, 148, 0,
            255, 144, 0,
            255, 140, 0,
            255, 136, 0,
            255, 132, 0,
            255, 128, 0,
            255, 124, 0,
            255, 120, 0,
            255, 116, 0,
            255, 112, 0,
            255, 108, 0,
            255, 104, 0,
            255, 100, 0,
            255, 96, 0,
            255, 92, 0,
            255, 88, 0,
            255, 84, 0,
            255, 80, 0,
            255, 72, 0,
            255, 68, 0,
            255, 64, 0,
            255, 60, 0,
            255, 56, 0,
            255, 52, 0,
            255, 48, 0,
            255, 44, 0,
            255, 40, 0,
            255, 36, 0,
            255, 32, 0,
            255, 28, 0,
            255, 24, 0,
            255, 20, 0,
            255, 16, 0,
            255, 12, 0,
            255, 8, 0,
            255, 4, 0,
            255, 0, 0,
        ])

        #self.image.save('output/temp/temp.png')
        #self.image = Image.open('output/temp/temp.png')

        self.image = Image.blend(self.image.convert("RGBA"), self.krakow_map.convert("RGBA"), 0.2)

        self.image.save('output\HeatMap_' + datetime.datetime.fromtimestamp(timestamp).strftime('%H_%M') + '.png')

