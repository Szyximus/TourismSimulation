import pyglet


class Agent:

    def __init__(self, position=(0, 0), velocity=(0, 0)):

        # position (x,y)
        # velocity (x,y)
        self.position = position
        self.velocity = velocity
        self.sprite = pyglet.sprite.Sprite(pyglet.image.load('./graphics/Pin.png'), x=position[0], y=position[1])

    def draw(self, window_position):
        self.sprite.x = self.relative_position(window_position)[0]
        self.sprite.y = self.relative_position(window_position)[1]
        self.sprite.draw()

    def relative_position(self, window_position):
        return (window_position[0] + self.position[0],
                window_position[1] + self.position[1])

    def update(self, dt):
        self.position = (self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt)
