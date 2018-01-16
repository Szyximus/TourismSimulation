from random import randint

import pyglet

from src.path_finding.grid import Grid
from src.path_finding.point import Point
from src.path_finding.walkpath import Walkpath


class Agent:

    def __init__(self, simulation, posx, posy, age, wealth, domestic, education, strictness, intoxication, fear):
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
        self.speed = self.compute_speed()

        self.previous_move = (0, 0)
        self.grid = Grid(self.simulation.grid, self.simulation.size_x, self.simulation.size_y)

        self.schedule = []
        self.current_poi = None
        self.walkpath = None

        self.pixels_walked = 0
        self.inside_poi = False
        self.time_to_spend = None

        self.walking_img = pyglet.image.load('./graphics/Pin.png')
        #self.inside_poi_img = pyglet.image.load('./graphics/Pin2.png')
        self.img = self.walking_img
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    @staticmethod
    def generate(simulation, x, y, spawn_point):
        age = randint(5, 70)
        wealth = randint(0, 10)
        intoxication = randint(0, 10)
        domestic = randint(0, 1)
        education = randint(0, 10)
        strictness = randint(0, 10)
        fear = randint(0, 3)

        agent = Agent(simulation, x, y, age, wealth, domestic, education, strictness, intoxication, fear)
        agent._generate_schedule(simulation.scheduler.generate(agent, simulation.timebox.timestamp))
        agent.schedule.insert(0, spawn_point)
        return agent

    def _generate_schedule(self, schedule):
        self.schedule = schedule
        self.current_poi = self.schedule.pop()
        self.walkpath = Walkpath.from_agent(self)

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

        self.inside_poi = True
        print("Inside poi " + self.current_poi.name)
        self.time_to_spend = self.current_poi.time_needed * 60  # in seconds
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
        else: # shouldn't occur, last poi in schedule should be spawn_point
            self.current_poi = self.simulation.pois[randint(0, len(self.simulation.pois)-1)]
        #self.img = self.walking_img
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.posx
        self.sprite.y = windowy + self.posy
        self.sprite.draw()

    def update(self, simulation_delta_time):
        if self.inside_poi:
            if self.time_to_spend <= 1:
                self.poi_leaved()
            self.time_to_spend -= simulation_delta_time
            return

        if self.is_poi_reached():
            self.poi_reached()
            return

        next_x = self.posx
        next_y = self.posy
        seconds_counter = 0
        while seconds_counter < simulation_delta_time:
            seconds_counter += 1
            direction_x, direction_y = self.walkpath.get_direction(next_x, next_y)
            next_x += self.speed * direction_x
            next_y += self.speed * direction_y

        # (sqrt((self.posx - next_x)**2 + (self.posy - next_y)**2)) ~= self.speed * simulation_delta_time
        # print(sqrt((self.posx - next_x)**2 + (self.posy - next_y)**2), self.speed * simulation_delta_time)
        self.pixels_walked += self.speed * simulation_delta_time
        self.posx = round(next_x)
        self.posy = round(next_y)

    def is_poi_reached(self):
        distance_from_poi = Point(self.posx, self.posy).distance_from(Point(self.current_poi.x, self.current_poi.y))
        # TODO hardcoded precision, may be moved to configs
        # cannot be lower than step in path-finding-algorithm
        if distance_from_poi < 16:
            if self.current_poi.is_end_point:
                self.simulation.agents.remove(self)
            return True
        return False
