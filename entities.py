import pyglet

class Entity(object):
    def __init__(self, location ):
        self.location = location



class Wall(Entity):
    def draw(self, px, py, size):

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
            [0,1,2,3],
            ('v2i', (px, py,
             px+size, py,
             px+size, py+size,
             px, py+size)),
             ('c3B', (0, 0, 255, 0, 255, 0, 255, 0, 0, 128,128,128))
)

class Player(Entity):
    def draw(self, px, py, size):
        size = size * .75
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
            [0,1,2,3],
            ('v2f', (px, py,
                    px+size, py,
                    px+size, py+size,
                    px, py+size)),
             ('c3B',
                    (255, 255, 0,
                    255, 255, 0,
                    255, 255, 0,
                    255,255,0)))
