import pyglet
import input

class Board(object):

    #           this, from left, up from bottom, size of grid square
    def __init__(self, x, y, pixels, layout):
        self.x = x
        self.y = y
        self.pxPerGrid = pixels
        self.entities = layout.entities;
        self.player = layout.player;

    def draw(self):
        for entity in self.entities:
            entity.draw(entity.location[0]*self.pxPerGrid + self.x,
                        entity.location[1]*self.pxPerGrid + self.y,
                        self.pxPerGrid )

    def command(self, cmd):
        self.player.setDirection(cmd)

    def findAdjacentEntities(self, location, direction):
        if ( direction == input.Input.MOVE_UP):
            adjacent = (location[0], location[1]+1);
        elif ( direction == input.Input.MOVE_DOWN):
            adjacent = (location[0], location[1]-1);
        elif ( direction == input.Input.MOVE_RIGHT):
            adjacent = (location[0]+1, location[1]);
        elif ( direction == input.Input.MOVE_LEFT):
            adjacent = (location[0]-1, location[1]);

        for entity in self.entities:
            if ( entity.location == adjacent ):
                return entity;

    def updateTick(self):
        self.player.tick(
            self.findAdjacentEntities(
                self.player.location,
                self.player.direction))
