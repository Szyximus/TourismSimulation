import pyglet


class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(resizable=True, caption='Tourism Simulation', visible= False)
        self.set_minimum_size(226, 354)
        self.set_maximum_size(2260, 3540)
        self.set_visible(True)
        self.krakow_map = pyglet.image.load('graphics\Krk.png')
        self.krakow_map.anchor_x = self.krakow_map.width // 2
        self.krakow_map.anchor_y = self.krakow_map.height // 2

        self.label = pyglet.text.Label(
            'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek', font_name='Verdana',
            font_size=8, x=self.width - 8,
            y=4, anchor_x='right', anchor_y='bottom')
        self.labelShadow = pyglet.text.Label(
            'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek', font_name='Verdana',
            font_size=8, x=self.width - 7, color=(0, 0, 0, 128),
            y=3, anchor_x='right', anchor_y='bottom')

        self.x = 1100
        self.y = 1200

    def on_draw(self):
        self.clear()

        self.label = pyglet.text.Label(
            'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek',
            font_name='Verdana', font_size=8, x=self.width - 8, y= 4,
            anchor_x='right', anchor_y='bottom')
        self.labelShadow = pyglet.text.Label(
            'Modelowanie i symulacja systemów, Szymon Jakóbczyk, Mateusz Kuźmik, Paweł Płatek', font_name='Verdana',
            font_size=8, x=self.width - 7, color=(0, 0, 0, 128),
            y=3, anchor_x='right', anchor_y='bottom')

        self.krakow_map.blit(self.width // 2,self.height // 2)

        self.labelShadow.draw()
        self.label.draw()



if __name__ == '__main__':

    window = Window()
    pyglet.app.run()
