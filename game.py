import gameTick
import input

class Game(object):

    BASE_TICK_SPEED = 0.01

    def __init__(self, board, input, infoDisplay):
        self.score = 0
        self.lives = 3
        self.lost = False
        self.paused = False
        self.tickSpeed = Game.BASE_TICK_SPEED
        self.ticker = gameTick.GameTick()
        self.board = board
        self.input = input
        self.infoDisplay = infoDisplay

    def togglePause(self):
        self.paused = not self.paused
        self.infoDisplay.showPausedLabel = self.paused

    def gameTick(self, dt):
        if self.lost:
            self.infoDisplay.showGameoverLabel = True
        else:
            command = self.input.consume()
            if command == input.Input.TOGGLE_PAUSE:
                self.togglePause()
            if not self.paused:
                if command and command != input.Input.TOGGLE_PAUSE:
                    self.board.command(command)

                if self.ticker.isTick(self.tickSpeed):
                    scoreDelta, livesDelta = self.board.updateTick()
                    self.score += scoreDelta
                    self.lives += livesDelta

        if ( self.lives < 1 ):
            self.lost = True;

    def draw(self):
        self.board.draw()
        self.infoDisplay.draw(self.score, self.lives)
