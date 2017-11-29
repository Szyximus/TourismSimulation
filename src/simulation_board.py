import pyglet

class SimulationBoard:

    def __init__(self):
        self.agents = [];

    def add_agent(self, agent):
        self.agents.append(agent)

