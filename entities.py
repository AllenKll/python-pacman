import pyglet
import input

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

    direction = input.Input.MOVE_LEFT
    percentX = 0.50
    percentY = 0.50
    moveSpeed = 0.10
    characterPercent = 0.70
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
        if ( (self.direction == input.Input.MOVE_LEFT or
              self.direction == input.Input.MOVE_RIGHT ) and
             (cmd == input.Input.MOVE_LEFT or
              cmd == input.Input.MOVE_RIGHT )):
              self.direction = cmd
        elif ( (self.direction == input.Input.MOVE_UP or
              self.direction == input.Input.MOVE_DOWN ) and
             (cmd == input.Input.MOVE_UP or
              cmd == input.Input.MOVE_DOWN )):
              self.direction = cmd
        else:
            self.queuedCmd = cmd;
            print "command queued"


    def tick(self, entity):
        if ( self.direction == input.Input.MOVE_LEFT ):
            self.percentX -= self.moveSpeed
            if ( isinstance(entity, Wall) and self.percentX < 0.5 ):
                self.percentX = 0.5
        elif ( self.direction == input.Input.MOVE_RIGHT ):
            self.percentX += self.moveSpeed
            if ( isinstance(entity, Wall) and self.percentX > 0.5 ):
                self.percentX = 0.5
        elif ( self.direction == input.Input.MOVE_UP ):
            self.percentY += self.moveSpeed
            if ( isinstance(entity, Wall) and self.percentY > 0.5 ):
                self.percentY = 0.5
        elif ( self.direction == input.Input.MOVE_DOWN ):
            self.percentY -= self.moveSpeed
            if ( isinstance(entity, Wall) and self.percentY < 0.5 ):
                self.percentY = 0.5

        if (( self.queuedCmd == input.Input.MOVE_UP or
              self.queuedCmd == input.Input.MOVE_DOWN) and
              self.percentX == 0.50):
             self.direction = self.queuedCmd
             self.queuedCmd = None
        elif ((self.queuedCmd == input.Input.MOVE_RIGHT or
               self.queuedCmd == input.Input.MOVE_LEFT) and
               self.percentY == 0.50):
             self.direction = self.queuedCmd
             self.queuedCmd = None

        if ( self.percentX > 1.0):
            self.location = (self.location[0] + 1, self.location[1])
            self.percentX = 0.0 + self.moveSpeed
        elif ( self.percentX < 0.0):
            self.location = (self.location[0] - 1, self.location[1])
            self.percentX = 1.0 - self.moveSpeed
        elif ( self.percentY > 1.0):
            self.location = (self.location[0], self.location[1] + 1)
            self.percentY = 0.0 + self.moveSpeed
        elif ( self.percentY < 0.0):
            self.location = (self.location[0], self.location[1] - 1)
            self.percentY = 1.0 - self.moveSpeed
