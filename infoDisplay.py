import pyglet

class InfoDisplay(object):
    ''' display of text messages '''
    SCORE_X = 10
    STATUS_Y = 470
    LIVES_X = 630

    def __init__(self, window):
        self.scoreLabel = pyglet.text.Label('',  font_size=14,
                                            x=InfoDisplay.SCORE_X,
                                            y=InfoDisplay.STATUS_Y,
                                            anchor_x = 'left',
                                            anchor_y = 'top')

        self.livesLabel = pyglet.text.Label('',  font_size=14,
                                            x=InfoDisplay.LIVES_X,
                                            y=InfoDisplay.STATUS_Y,
                                            anchor_x = 'right',
                                            anchor_y = 'top')

        self.pausedLabel = pyglet.text.Label('PAUSED',
                                             font_size=32,
                                             x=window.width // 2,
                                             y=window.height // 2,
                                             anchor_x='center',
                                             anchor_y='center')
        self.pausedLabel.set_style('background_color', (0,0,0,127))

        self.gameoverLabel = pyglet.text.Label('GAME OVER',
                                                font_size=32,
                                                x=window.width // 2,
                                                y=window.height // 2,
                                                anchor_x='center',
                                                anchor_y='center')
        self.gameoverLabel.set_style('background_color', (0,0,0,127))

        self.showPausedLabel = False
        self.showGameoverLabel = False

    def draw(self, score, lives):
        self.scoreLabel.text = "Score " + str(score)
        self.livesLabel.text = "Lives " + str(lives)

        self.scoreLabel.draw()
        self.livesLabel.draw()
        if self.showPausedLabel:
            self.pausedLabel.draw()
        if self.showGameoverLabel:
            self.gameoverLabel.draw()
