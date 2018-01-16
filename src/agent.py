import pyglet
from random import randint
from src.path_finding.walkpath import Walkpath
from src.path_finding.point import Point
from src.path_finding.grid import Grid


class Agent:

    def __init__(self, simulation, posx, posy, age, wealth, domestic, education, strictness, intoxication, fear, schedule):
        self.posx = posx
        self.posy = posy

        self.simulation = simulation

        self.age = age
        self.wealth = wealth
        self.domestic = domestic
        self.education = education
        self.strictness = strictness
        self.intoxication = intoxication
        self.fear = fear
        self.schedule = schedule

        self.speed = self.compute_speed()
        self.current_poi = self.schedule.pop()
        self.previous_move = (0, 0)
        self.grid = Grid(self.simulation.grid, self.simulation.size_x, self.simulation.size_y)
        self.walkpath = Walkpath.from_agent(self)

        self.inside_poi = False
        self.time_to_spend = None

        self.walking_img = pyglet.image.load('./graphics/Pin.png')
        #self.inside_poi_img = pyglet.image.load('./graphics/Pin2.png')
        self.img = self.walking_img
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    def compute_speed(self):
        """ Returns amount of pixels that the agent should move in one simulation second
            Normal speed is about 1.4 meters per second
        """
        speed = 1.4
        if self.age < 14 or self.age > 60:
            speed -= 0.7
        if 18 < self.age < 24:
            speed += 0.7
        return round(speed * self.simulation.pixels_per_meter)

    def poi_reached(self):
        self.posx = self.current_poi.x
        self.posy = self.current_poi.y

        base_probability_to_enter_poi = 80
        if (self.wealth - self.current_poi.price)*10 < base_probability_to_enter_poi:
            self.next_poi()
            return

        self.inside_poi = True
        print("Inside poi " + self.current_poi.name)
        self.time_to_spend = round(self.current_poi.time_needed / self.simulation.time_speed)
        #self.img = self.inside_poi_img
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    def next_poi(self):
        if len(self.schedule) > 0:
            self.current_poi = self.schedule.pop()
            self.walkpath = Walkpath.from_agent(self)

    def poi_leaved(self):
        self.inside_poi = False
        print("Leave poi " + self.current_poi.name)
        if len(self.schedule) > 0:
            self.current_poi = self.schedule.pop()
        else:
            self.current_poi = self.simulation.pois[randint(0, len(self.simulation.pois)-1)]
        #self.img = self.walking_img
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.posx
        self.sprite.y = windowy + self.posy
        self.sprite.draw()

    def calculate_direction(self, new_tmp_target):
        min_distance_to_walk = randint(5, 100)

        direction_x = 0
        precision = 10
        if new_tmp_target[0] - precision > self.posx:
            direction_x = 1
        elif new_tmp_target[0] < self.posx - precision:
            direction_x = -1

        direction_y = 0
        if new_tmp_target[1] - precision > self.posy:
            direction_y = 1
        elif new_tmp_target[1] < self.posy - precision:
            direction_y = -1

        destination = (direction_x*min_distance_to_walk, direction_y*min_distance_to_walk)
        if self.simulation.grid[destination[1]][destination[0]] == 0:
            if abs(self.posx - self.current_poi.x) > abs(self.posy - self.current_poi.y):
                if randint(0, 3) != 0:
                    direction_y = (direction_y + 1) % 2
                else:
                    direction_x = (direction_x + 1) % 2
            else:
                if randint(0, 4) != 0:
                    direction_x = (direction_x + 1) % 2
                else:
                    direction_y = (direction_y + 1) % 2
        return direction_x, direction_y

    def update(self, simulation_delta_time):
        if self.inside_poi:
            if self.time_to_spend == 1:
                self.poi_leaved()
            self.time_to_spend -= 1
            return

        if self.is_poi_reached():
            self.poi_reached()
            return

        next_x = self.posx
        next_y = self.posy
        seconds_counter = 0

        print(simulation_delta_time, self.speed)
        while seconds_counter < simulation_delta_time:
            # simulation_delta_time is seconds from last update, speed is pixels per second, so we move agent
            # as much we can in computed direction until seconds pass or we hit wall (then we compute new direction)
            direction_x, direction_y = self.walkpath.get_direction(next_x, next_y)
            print(direction_x, direction_y)
            while True:
                seconds_counter += 1
                next_x += self.speed * direction_x
                next_y += self.speed * direction_y
                if self.simulation.grid[round(next_y)][round(next_x)] == 1 or seconds_counter >= simulation_delta_time:
                    break

        print(abs(self.posx - next_x), abs(self.posy - next_y))
        print(next_x, next_y)
        self.posx = round(next_x)
        self.posy = round(next_y)
        print('_-----------------')

    def is_poi_reached(self):
        distance_from_poi = Point(self.posx, self.posy).distance_from(Point(self.current_poi.x, self.current_poi.y))
        # TODO hardcoded precision, may be moved to configs
        # cannot be lower than step in path-finding-algorithm
        return distance_from_poi < 16


def random_true(probability):
    if probability > 1 or probability < 0:
        raise ValueError('Value of probability is out of 0 and 1.')
    if randint(0,100) < probability*100:
            return True
    else:
        return False