import pyglet

from map import Map


class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(resizable=True, caption='Tourism Simulation', visible= False)
        self.set_minimum_size(226, 354)
        self.set_maximum_size(2260, 3540)
        self.frame_rate = 1/60.0

        self.map = Map(self.width, self.height)
        self.set_visible(True)

        self.x = 1100
        self.y = 1200

    def on_draw(self):
        self.clear()
        self.map.draw(self.width, self.height, self.x, self.y)





if __name__ == '__main__':

    window = Window()
    #pyglet.clock.schedule_interval(window.on_draw(), window.frame_rate)
    pyglet.app.run()
