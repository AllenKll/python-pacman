import pyglet

class Board(object):

    #           this, from left, up from bottom, size of grid square
    def __init__(self, x, y, pixels):
        self.x = x
        self.y = y
        self.pxPerGrid = pixels
        self.entities = [];

    def draw(self):
        for entity in self.entities:
            entity.draw(entity.location[0]*self.pxPerGrid + self.x,
                        entity.location[1]*self.pxPerGrid + self.y,
                        self.pxPerGrid )
