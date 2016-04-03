import entities

class Loader(object):

    # generates a 2D array representing the map of the Board
    # given a layout file.
    def __init__(self, filename):
        f = open(filename, 'r')
        self.map = []
        x = 0
        y = 0

        for line in f:
            x = 0
            currentLine = []
            for c in line:
                if c == '#':
                    break;
                elif c == '.':
                    currentLine.append( entities.Pellet())
                elif c == 'W' or c == 'w':
                    currentLine.append( entities.Wall())
                elif c == 'P' or c == 'p':
                    self.player =  entities.Player((x,y))
                    currentLine.append(entities.Floor())
                else: # space!!....
                    currentLine.append(entities.Floor())
                x += 1

            if (c != '#'):
                y = y + 1;
                self.map.append(currentLine)
