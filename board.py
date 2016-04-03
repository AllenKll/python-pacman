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
        self.playerDirection = input.Input.MOVE_LEFT;
        self.queuedDirection = None;
        self.gulp = pyglet.media.load('eating.wav', streaming=False)


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
        self.queuedDirection = cmd

    def isCollision(self, location, className):
        if ( type(self.map[location[1]][location[0]]) is className ):
            return True
        return False

    def directionIsValid(self, direction, location):
        if ( direction == input.Input.MOVE_LEFT and
             not self.isCollision( (location[0]-1, location[1]), entities.Wall)):
            return True;
        elif ( direction == input.Input.MOVE_RIGHT and
               not self.isCollision( (location[0]+1, location[1]), entities.Wall )):
            return True;
        elif ( direction == input.Input.MOVE_UP and
               not self.isCollision( (location[0], location[1]+1), entities.Wall )):
            return True;
        elif ( direction == input.Input.MOVE_DOWN and
               not self.isCollision( (location[0], location[1]-1), entities.Wall )):
            return True;
        return False

    def updateTick(self):
        if ( self.queuedDirection != None and
             self.directionIsValid(self.queuedDirection,
                               self.playerLocation) ):
            self.player.move(self.queuedDirection)
            self.playerDirection = self.queuedDirection
        elif (self.directionIsValid(self.playerDirection,
                               self.playerLocation)):
            self.player.move(self.playerDirection)
        else:
            self.player.move(None)

        location = self.player.tick()

        self.playerLocation = location
        if ( self.isCollision ( self.playerLocation, entities.Pellet )):
            self.map[self.playerLocation[1]][self.playerLocation[0]] = entities.Floor();
            self.gulp.play()
