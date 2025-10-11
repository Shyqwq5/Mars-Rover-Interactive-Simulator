from src.compass_direction import CompassDirection

class Rover:
    def __init__(self,name,direction):
        self.direction = direction
        self.name = name

    def turn_left(self):
        dict = {CompassDirection.NORTH:CompassDirection.WEST,CompassDirection.WEST:CompassDirection.SOUTH,CompassDirection.SOUTH:CompassDirection.EAST,CompassDirection.EAST:CompassDirection.NORTH}
        self.direction = dict[self.direction]

    def turn_right(self):
        dict = {CompassDirection.NORTH:CompassDirection.EAST,CompassDirection.EAST:CompassDirection.SOUTH,CompassDirection.SOUTH:CompassDirection.WEST,CompassDirection.WEST:CompassDirection.NORTH}
        self.direction = dict[self.direction]

    def move(self,position):
        if self.direction == CompassDirection.NORTH:
            return (position[0],position[1]+1)
        if self.direction == CompassDirection.SOUTH:
            return (position[0],position[1]-1)
        if self.direction == CompassDirection.EAST:
            return (position[0]+1,position[1])
        if self.direction == CompassDirection.WEST:
            return (position[0]-1,position[1])



