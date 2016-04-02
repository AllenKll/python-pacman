import pyglet
import loader
import board
import game
import input

window = pyglet.window.Window(640,480)

layout = loader.Loader(filename = "level1.layout")
theBoard = board.Board(x = 10, y = 10, pixels = 20, layout=layout)
theInput = input.Input()
theGame = game.Game(theBoard, theInput)

@window.event
def on_draw():
    window.clear()
    theBoard.draw()

@window.event
def on_key_press(symbol, modifiers):
    theInput.doKeypress(symbol, modifiers)

@window.event
def on_text_motion(motion):
    theInput.doTextMotion(motion)

def systemTick(dt):
    theGame.gameTick(dt)

pyglet.clock.schedule_interval( systemTick, 1.0/60)

pyglet.app.run()
