import pyglet
from random import randint
import numpy as np


class Agent:

    def __init__(self, simulation, posx, posy, age, wealth, concentration, intoxication, schedule):
        self.posx = posx
        self.posy = posy

        self.simulation = simulation

        self.age = age
        self.wealth = wealth
        self.concentration = concentration
        self.intoxication = intoxication
        self.schedule = schedule

        self.speed = self.compute_speed()
        self.current_poi = self.schedule[0]
        self.previous_move = (0, 0)

        self.img = pyglet.image.load('./graphics/Pin.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    def compute_speed(self):
        # normal speed is about 1.4 meters per second
        speed = 1.4
        if self.age < 14 or self.age > 60:
            speed -= 0.7
        if 18 < self.age < 24:
            speed += 0.7
        return round(speed * self.simulation.pixels_per_meter)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.posx
        self.sprite.y = windowy + self.posy
        self.sprite.draw()

    def something_on_the_way(self, sx, sy):
        checks = randint(5, 20)
        jump_x = (sx - self.posx) / checks
        jump_y = (sy - self.posy) / checks
        for jump in range(1, checks+1):
            px = min(round(self.posx + (self.simulation.size_x // 2) + (jump_x * jump)), self.simulation.size_x-1)
            py = min(round(self.posy + (self.simulation.size_y // 2) + (jump_y * jump)), self.simulation.size_y-1)
            if self.simulation.map_raster[py][px] == 0:
                return True
        return False

    def find_new_tmp_target(self):
        checks_x, checks_y = randint(5, 30), randint(5, 30)
        new_target_x, new_target_y = self.current_poi.x, self.current_poi.y
        jump_size = randint(10, 50)
        for jump_x in range(checks_x):
            for jump_y in range(checks_y):
                if not self.something_on_the_way(new_target_x + jump_x * jump_size, new_target_y + jump_y * jump_size):
                    return new_target_x + jump_x * jump_size, new_target_y + jump_y * jump_size
                if not self.something_on_the_way(new_target_x + jump_x * jump_size, new_target_y - jump_y * jump_size):
                    return new_target_x + jump_x * jump_size, new_target_y - jump_y * jump_size
                if not self.something_on_the_way(new_target_x - jump_x * jump_size, new_target_y + jump_y * jump_size):
                    return new_target_x - jump_x * jump_size, new_target_y + jump_y * jump_size
                if not self.something_on_the_way(new_target_x - jump_x * jump_size, new_target_y - jump_y * jump_size):
                    return new_target_x - jump_x * jump_size, new_target_y - jump_y * jump_size
        return self.current_poi.x, self.current_poi.y

    def calculate_direction(self, new_tmp_target):
        direction_x = 0
        if new_tmp_target[0] > self.posx:
            direction_x = 1
        elif new_tmp_target[0] < self.posx:
            direction_x = -1

        direction_y = 0
        if new_tmp_target[1] > self.posy:
            direction_y = 1
        elif new_tmp_target[1] < self.posy:
            direction_y = -1

        return direction_x, direction_y

    def calculate_distance(self, target):
        return (target[0] - self.posx)*(target[0] - self.posx) + (target[1] - self.posy)*(target[1] - self.posy)

    def update(self, dt):
        # looking around  - not work
        # if self.previous_move == (0, 0):
        #     new_tmp_target = self.find_new_tmp_target()
        #     print(new_tmp_target, (self.current_poi.x, self.current_poi.y))
        #     self.previous_move = self.calculate_direction(new_tmp_target)

        change_route_probability = 20

        if self.previous_move == (0, 0) or randint(0, 100) <= change_route_probability:
            direction_x, direction_y = self.calculate_direction((self.current_poi.x, self.current_poi.y))
        else:
            direction_x, direction_y = self.previous_move

        new_pos_x = self.posx + self.speed * direction_x
        new_pos_y = self.posy + self.speed * direction_y
        if self.simulation.map_raster[new_pos_y + (self.simulation.size_y // 2)][new_pos_x + (self.simulation.size_x // 2)] == 0:
            self.previous_move = (randint(0,2)-1, randint(0,2)-1)
        else:
            self.posx += self.speed * direction_x
            self.posy += self.speed * direction_y
            self.previous_move = (direction_x, direction_y)

