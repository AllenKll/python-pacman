import entities

class Loader(object):

    def __init__(self, filename):
        f = open(filename, 'r')
        self.grid = []
        x = 0
        y = 0

        for line in f:
            x = 0
            currentLine = []
            for c in line:
                if c == '#':
                    break;
                elif c == 'W':
                    currentLine.append( entities.Wall(location = (x, y)))
                elif c == 'P':
                    currentLine.append( entities.Player(location = (x, y)))
                x += 1

            if (c != '#'):
                y = y + 1;
                self.grid.extend(currentLine)
