import pyglet

class Agent:

    def __init__(self, posx, posy, velx, vely):

        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.img = pyglet.image.load('./graphics/Pin.png')
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)

    def draw(self, windowx, windowy):
        self.sprite.x = windowx + self.posx
        self.sprite.y = windowy + self.posy
        self.sprite.draw()

    def update(self, dt):
        self.posx += self.velx * dt
        self.posy += self.vely * dt