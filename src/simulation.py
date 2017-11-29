import pyglet
from agent import Agent
from spawn_point import SpawnPoint
from point_of_interest import PointOfInterest


class Simulation:

    def __init__(self):
        self.agents = []
        self.spawn_points = [SpawnPoint(-990, 1300, 'Teatr Bagatela', 1),
                             SpawnPoint(-900, 540, 'Filharmonia', 0.2),
                             SpawnPoint(-430, 555, 'Plac Wszystkich Świętych', 0.5),
                             SpawnPoint(35, 625, 'Poczta Główna', 0.8),
                             SpawnPoint(350, 1450, 'Dworzec Główny', 0.5),
                             SpawnPoint(-270, 1750, 'Stary Kleparz', 0.2)]

        self.pois = [PointOfInterest(-660, 1070, 'McDonald\'s', 5, 2, 4),
                     PointOfInterest(-480, 990, 'Sukiennice', 7, 0, 2),
                     PointOfInterest(-575, 1125, 'Polonia Wax Museum', 2, 8, 5),
                     PointOfInterest(-540, 1200, 'Bobby Burger', 6, 5, 4),
                     PointOfInterest(-310, 982, 'Bazylika Mariacka', 3, 0, 8),
                     PointOfInterest(-410, 955, 'Pomnik Adama Mickiewicza', 2, 0, 1),
                     PointOfInterest(-315, 1080, 'Pijalnia Czekolady E. Wedel', 6, 7, 6),
                     PointOfInterest(-438, 854, 'Kościół Świętego Wojciecha', 2, 0, 5),
                     PointOfInterest(-585, 955, 'Wieża Ratuszowa', 2, 1, 3)]



    def update(self, dt):
        list(map(lambda spawn_point: spawn_point.update(self.agents), self.spawn_points))
        list(map(lambda agent: agent.update(dt), self.agents))

    def draw(self, windowx, windowy):
        list(map(lambda agent: agent.draw(windowx, windowy), self.agents))
        list(map(lambda spawn: spawn.draw(windowx, windowy), self.spawn_points))
        list(map(lambda poi: poi.draw(windowx, windowy), self.pois))

