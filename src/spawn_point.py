import pyglet
import time
from src.agent import Agent
from random import randint
from src.poilabel import PoiLabel
from src.schedules_generator import SchedulesGenerator


def current_milli_time():
    return int(round(time.time() * 1000))


class SpawnPoint:

    def __init__(self, x, y, name, agents_per_min):
        self.x = x
        self.y = y
        self.agents_per_min = agents_per_min
        self.name = name


        self.last_activation_time = current_milli_time()

        self.img = pyglet.image.load('./graphics/Spawn.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

        self.label = PoiLabel(name, x, y)

        self.counter = int(33 / agents_per_min)
        self.i = self.counter

    @classmethod
    def from_dict(cls, name, attributes):
        required_all = ["x", "y", "agents_per_min"]
        for required in required_all:
            if required not in attributes.keys():
                raise ValueError("Required key in spawn points config file not found: {}".format(required))

        if name == "" or name is None:
            raise ValueError("Name can't be empty")
        attributes["name"] = name
        
        return SpawnPoint(**attributes)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.x
        self.sprite.y = windowy + self.y
        self.sprite.draw()
        self.label.draw(self.sprite.x, self.sprite.y)

    def update(self, dt, simulation):
        self.i -= 1
        schedules_generator = SchedulesGenerator(simulation.pois)
        if self.i == 0:
            self.i = self.counter
            age = randint(5, 70)
            wealth = randint(0, 10)
            concentration = randint(10, 100)
            intoxication = randint(0, 20)
            domestic = 0
            education = 0
            strictness = 0
            fear = None
            schedule = schedules_generator.generate()
            simulation.agents.append(Agent(simulation, self.x, self.y, age, wealth, domestic, education, strictness,
                                           intoxication, fear, schedule))
            pass
