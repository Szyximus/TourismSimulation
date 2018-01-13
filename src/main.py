import pyglet
from pyglet.window import mouse
from src.map import Map
from src.simulation import Simulation

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(resizable=True, caption='Tourism Simulation', visible=False)
        self.set_minimum_size(640, 480)
        self.set_maximum_size(2260, 3540)
        self.frame_rate = 1/60.0

        self.map = Map(self.width, self.height)
        self.set_visible(True)

        self.x = 800
        self.y = -800

        self.simulation = Simulation(2260, 3540, self.width, self.height, 'configs/config.yaml')

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if (buttons & mouse.LEFT) or (buttons & mouse.MIDDLE):
            self.x = self.x + dx
            self.y = self.y + dy
            if self.x > 1120:
                self.x = 1120
                pass

            if self.x < self.width - 1120:
                self.x = self.width - 1120
                pass

            if self.y > 1760:
                self.y = 1760
                pass
            pass

        if self.y < self.height - 1760:
            self.y = self.height - 1760
            pass

    def update(self, dt):
        self.simulation.update(dt)

    def on_draw(self):
        self.clear()
        self.map.draw(self.width, self.height, self.x, self.y)
        self.simulation.draw(self.x, self.y)


if __name__ == '__main__':

    window = Window()
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
