import pyglet
import input

class Wall(object):
    def draw(self, px, py, size):

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
            [0,1,2,3],
            ('v2i', (px, py,
             px+size, py,
             px+size, py+size,
             px, py+size)),
             ('c3B', (0, 0, 255, 0, 255, 0, 255, 0, 0, 128,128,128))
)

class Floor(object):
    def draw(self, px, py, size):
        pass


class Player(object):

    def __init__(self, location):
        self.location = location

    direction = input.Input.MOVE_LEFT
    percentX = 0.50          # initial % location in grid
    percentY = 0.50
    moveSpeed = 0.10         # percent of grit to move per tick
    characterPercent = 0.70  # size comapred to grid
    moveX = 0                # the active moving direction
    moveY = 0
    queuedCmd = None

    def draw(self, px, py, size):
        realX = px + ( self.percentX * size)
        realY = py + ( self.percentY * size)
        realSize = size * self.characterPercent
        halfSize = realSize / 2.0

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
            [0,1,2,3],
            ('v2f', (realX-halfSize, realY-halfSize,
                    realX-halfSize, realY+halfSize,
                    realX+halfSize, realY+halfSize,
                    realX+halfSize, realY-halfSize)),
            ('c3B',
                    (255, 255, 0,
                    255, 255, 0,
                    255, 255, 0,
                    255,255,0)))

    def setDirection(self, cmd):
        self.queuedCmd = cmd

    def stop(self, location):
        self.location = location
        self.percentX = .5
        self.percentY = .5
        self.direction = None

    def tick(self, validLocations):
        # if we're in the middle of the square, we can decide
        # if movement is valid
        if ( self.percentY == .5 and self.percentX == .5):
            # if direction change, check for valid
            if ( self.queuedCmd != None ):
                if ( self.queuedCmd == input.Input.MOVE_LEFT and
                     (self.location[0]-1, self.location[1]) in validLocations):
                     self.moveX = 0 - self.moveSpeed
                     self.moveY = 0
                     self.queuedCmd = None
                elif ( self.queuedCmd == input.Input.MOVE_RIGHT and
                      (self.location[0]+1, self.location[1]) in validLocations):
                     self.moveX = 0 + self.moveSpeed
                     self.moveY = 0
                     self.queuedCmd = None
                elif ( self.queuedCmd == input.Input.MOVE_UP and
                      (self.location[0], self.location[1]+1) in validLocations):
                     self.moveX = 0
                     self.moveY = 0 + self.moveSpeed
                     self.queuedCmd = None
                elif ( self.queuedCmd == input.Input.MOVE_DOWN and
                      (self.location[0], self.location[1]-1) in validLocations):
                     self.moveX = 0
                     self.moveY = 0 - self.moveSpeed
                     self.queuedCmd = None

        self.percentX += self.moveX
        self.percentY += self.moveY

        if ( self.percentX > 1.0):
            self.location = (self.location[0] + 1, self.location[1])
            self.percentX = 0.0
        elif ( self.percentX < 0.0):
            self.location = (self.location[0] - 1, self.location[1])
            self.percentX = 1.0
        elif ( self.percentY > 1.0):
            self.location = (self.location[0], self.location[1] + 1)
            self.percentY = 0.0
        elif ( self.percentY < 0.0):
            self.location = (self.location[0], self.location[1] - 1)
            self.percentY = 1.0

        return self.location
