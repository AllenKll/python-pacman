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
             ('c3B', (0,0,255, 0,0,255, 0,0,255, 0,0,255))
)

class Floor(object):
    def draw(self, px, py, size):
        pass

class Pellet(object):
    characterPercent = 0.10

    def draw(self, px, py, size):
        realX = px + ( size / 2.0 )
        realY = py + ( size / 2.0 )
        realSize = size * self.characterPercent
        halfSize = realSize / 2.0

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
            [0,1,2,3],
            ('v2f', (realX-halfSize, realY-halfSize,
                     realX-halfSize, realY+halfSize,
                     realX+halfSize, realY+halfSize,
                     realX+halfSize, realY-halfSize)),
            ('c3B',
                    (255,255,255,
                     255,255,255,
                     255,255,255,
                     255,255,250)))

class Movable(object):
    def __init__(self, location):
        self.location = location

    percentX = 50          # initial % location in grid
    percentY = 50
    moveSpeed = 25         # percent of grit to move per tick
                           # MUST HIT 50 IN MULTIPLES
    characterPercent = 0.70  # size comapred to grid
    moveX = 0                # the active moving direction
    moveY = 0
    queuedX = 0            # queued moving directions
    queuedX = 0

    def draw(self, x, y, size):
        pass

    def tick(self):
        # if we're in the middle of the square, we can decide
        # to change direction
        if ( self.percentY == 50 and self.percentX == 50):
            self.moveX = self.queuedX
            self.moveY = self.queuedY

        # move
        self.percentX += self.moveX
        self.percentY += self.moveY

        # handle grid changes due to move.
        if ( self.percentX > 100):
            self.location = (self.location[0] + 1, self.location[1])
            self.percentX -= 100
        elif ( self.percentX < 0):
            self.location = (self.location[0] - 1, self.location[1])
            self.percentX += 100
        elif ( self.percentY > 100):
            self.location = (self.location[0], self.location[1] + 1)
            self.percentY -= 100
        elif ( self.percentY < 0):
            self.location = (self.location[0], self.location[1] - 1)
            self.percentY += 100

        return self.location


class Player(Movable):

    def draw(self, px, py, size):
        realX = px + ( (self.percentX /100.0) * size)
        realY = py + ( (self.percentY /100.0) * size)
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

    def move(self, newDirection):
        if ( newDirection == input.Input.MOVE_LEFT):
            self.queuedX = 0 - self.moveSpeed
            self.queuedY = 0
        elif ( newDirection == input.Input.MOVE_RIGHT):
            self.queuedX = self.moveSpeed
            self.queuedY = 0
        elif ( newDirection == input.Input.MOVE_UP):
            self.queuedX = 0
            self.queuedY = self.moveSpeed
        elif ( newDirection == input.Input.MOVE_DOWN):
            self.queuedX = 0
            self.queuedY = 0 - self.moveSpeed
        else:  # stop
            self.queuedX = 0
            self.queuedY = 0

class Blinky(Player):

    def draw(self, px, py, size):
        realX = px + ( (self.percentX /100.0) * size)
        realY = py + ( (self.percentY /100.0) * size)
        realSize = size * self.characterPercent
        halfSize = realSize / 2.0

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
            [0,1,2,3],
            ('v2f', (realX-halfSize, realY-halfSize,
                    realX-halfSize, realY+halfSize,
                    realX+halfSize, realY+halfSize,
                    realX+halfSize, realY-halfSize)),
            ('c3B',
                    (255, 0, 0,
                    255, 0, 0,
                    255, 0, 0,
                    255, 0,0)))

    def think(self, playerLocation):
        pass
