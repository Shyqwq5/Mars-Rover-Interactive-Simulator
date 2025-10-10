from src.rover import Rover
from src.compass_direction import CompassDirection
#test turn directior
def test_turn_left():
    a_car = Rover()
    a_car.diection = CompassDirection.NORTH
    a_car.turn_left()
    assert a_car.diection == CompassDirection.WEST


