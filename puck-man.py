import pyglet
import loader
import board

window = pyglet.window.Window(640,480)

layout = loader.Loader(filename = "level1.layout")
b = board.Board(x = 10, y = 10, pixels = 20)
b.entities = layout.grid

@window.event
def on_draw():
    b.draw()

pyglet.app.run()
