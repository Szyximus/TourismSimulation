import pyglet
from pyglet.window import mouse
from src.map import Map
from src.simulation import Simulation

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(resizable=True, caption='Tourism Simulation', visible=False)
        self.set_minimum_size(640, 480)
        self.set_maximum_size(2260, 3540)
        self.frame_rate = 1/60

        self.map = Map(self.width, self.height)
        self.set_visible(True)

        self.x = 800
        self.y = -800

        self.label = pyglet.text.Label(
            "", font_name='Calibri',
            font_size=9, x=0,
            y=0, anchor_x='left', anchor_y='top')

        self.simulation = Simulation(2260, 3540, self.width, self.height)

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

    def on_mouse_press(self, x, y, button, modifiers):
        self.label = pyglet.text.Label(
            "x:" + str(self.x + x) + " y:" + str(self.y + y), font_name='Calibri',
            font_size=9, color=[255,0,0,255], x=x,
            y=y, anchor_x='left', anchor_y='top')

    def update(self, dt):
        self.simulation.update(dt)

    def on_draw(self):
        self.clear()
        self.map.draw(self.width, self.height, self.x, self.y)
        self.simulation.draw(self.x, self.y)
        self.label.draw()


if __name__ == '__main__':

    window = Window()
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
