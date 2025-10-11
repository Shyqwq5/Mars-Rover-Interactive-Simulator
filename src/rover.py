from src.compass_direction import CompassDirection

class Rover:
    def __init__(self):
        self.diection = None

    def turn_left(self):
        dict = {CompassDirection.NORTH:CompassDirection.WEST,CompassDirection.WEST:CompassDirection.SOUTH,CompassDirection.SOUTH:CompassDirection.EAST,CompassDirection.EAST:CompassDirection.NORTH}
        self.diection = dict[self.diection]

    def turn_right(self):
        dict = {CompassDirection.NORTH:CompassDirection.EAST,CompassDirection.EAST:CompassDirection.SOUTH,CompassDirection.SOUTH:CompassDirection.WEST,CompassDirection.WEST:CompassDirection.NORTH}
        self.diection = dict[self.diection]


