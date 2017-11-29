import pyglet
from agent import Agent


class Simulation:

    def __init__(self):
        self.agents=[]

    def generate_agent(self, posx=0, posy=0, velx=0, vely=0):
        self.agents.append(Agent(posx, posy, velx, vely))

    def update(self, dt):
        list(map(lambda agent: agent.update(dt), self.agents))

    def draw(self, windowx, windowy):
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
