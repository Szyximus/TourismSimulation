import time
from agent import Agent
from random import randint


def current_milli_time():
    return int(round(time.time() * 1000))


class SpawnPoint:

    def __init__(self, x, y, agents_per_sec):
        self.x = x
        self.y = y
        self.agents_per_sec = agents_per_sec

        self.last_activation_time = current_milli_time()

    def update(self, agents):
        agents.append(Agent(self.x, self.y, randint(-10, 10), randint(-10, 10)))