import pyglet
import input
import entities

class Board(object):

    #           this, from left, up from bottom, size of grid square
    def __init__(self, x, y, pixels, layout):
        self.x = x
        self.y = y
        self.pxPerGrid = pixels
        self.map = layout.map;
        self.player = layout.player;
        self.playerLocation = layout.player.location

    def draw(self):
        for y in range(0, len(self.map)):
            for x in range(0, len(self.map[y])):
                self.map[y][x].draw(x*self.pxPerGrid + self.x,
                                    y*self.pxPerGrid + self.y,
                                    self.pxPerGrid )

        self.player.draw(self.playerLocation[0] * self.pxPerGrid + self.x,
                         self.playerLocation[1] * self.pxPerGrid + self.y,
                         self.pxPerGrid)

    def command(self, cmd):
        self.player.setDirection(cmd)

    def isCollision(self, location):
        if ( type(self.map[location[1]][location[0]]) is entities.Wall ):
            return True
        return False

    def getValidDirections(self,location):
        # check the each direction
        locations = []
        if ( not self.isCollision( (location[0]+1, location[1]) )):
            locations.append( (location[0]+1, location[1]) )
        if ( not self.isCollision( (location[0]-1, location[1]) )):
            locations.append( (location[0]-1, location[1]) )
        if ( not self.isCollision( (location[0], location[1]+1) )):
            locations.append( (location[0], location[1]+1) )
        if ( not self.isCollision( (location[0], location[1]-1) )):
            locations.append( (location[0], location[1]-1) )
        return locations

    def updateTick(self):
        oldLocation = self.player.location
        location = self.player.tick(self.getValidDirections(oldLocation))

        self.playerLocation = location
        print self.playerLocation
