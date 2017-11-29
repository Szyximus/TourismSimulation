import pyglet
from agent import Agent


class Simulation:

    def __init__(self):
        self.agents = []

    def append_agent(self, position, velocity):
        self.agents.append(Agent(position, velocity))

    def update(self, dt):
        for agent in self.agents:
            agent.update(dt)

    def draw(self, window_position):
        for agent in self.agents:
            agent.draw(window_position)
