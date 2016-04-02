import entities

class Loader(object):

    def __init__(self, filename):
        f = open(filename, 'r')
        self.entities = []
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
                    self.player =  entities.Player(location = (x, y))
                    currentLine.append(self.player)
                x += 1

            if (c != '#'):
                y = y + 1;
                self.entities.extend(currentLine)
