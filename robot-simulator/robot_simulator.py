NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"



class Robot(object):
    _leftMap = {
        NORTH: WEST,
        SOUTH: EAST,
        EAST: NORTH,
        WEST: SOUTH
    }

    def __init__(self, bearing = NORTH, x_coord = 0, y_coord = 0):
        self.bearing = bearing
        self.coordinates = (x_coord, y_coord)

    def turn_left(self):
        self.bearing = self._leftMap[self.bearing]

    def turn_right(self):
        for _ in range(0, 3):
            self.turn_left()

    def advance(self):
        list_coordinates = list(self.coordinates)
        if (self.bearing == NORTH):
            list_coordinates[1] += 1
        elif (self.bearing == SOUTH):
            list_coordinates[1] -= 1
        elif (self.bearing == EAST):
            list_coordinates[0] += 1
        elif (self.bearing == WEST):
            list_coordinates[0] -= 1

        self.coordinates = tuple(list_coordinates)

    def simulate(self, sequence):
        list_sequence = list(sequence)
        for item in list_sequence:
            if (item == 'A'):
                self.advance()
            elif (item == 'L'):
                self.turn_left()
            elif (item == 'R'):
                self.turn_right()

