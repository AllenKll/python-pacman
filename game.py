import gameTick
import input

class Game(object):

    BASE_TICK_SPEED = 0.01

    def __init__(self, board, input):
        self.score = 0;
        self.lost = False;
        self.paused = False;
        self.tickSpeed = Game.BASE_TICK_SPEED
        self.ticker = gameTick.GameTick()
        self.board = board
        self.input = input

    def togglePause(self):
        self.paused = not self.paused

    def gameTick(self, dt):
#        if self.lost:
#            self.infoDisplay.showGameoverLabel = True
#        else:
            command = self.input.consume()
            if command == input.Input.TOGGLE_PAUSE:
                self.togglePause()
            if not self.paused:
                if command and command != input.Input.TOGGLE_PAUSE:
                    self.board.command(command)

                if self.ticker.isTick(self.tickSpeed):
                    self.lost = self.board.updateTick()
