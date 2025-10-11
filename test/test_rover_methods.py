from src.logic_layer.rover import Rover
from src.compass_direction import CompassDirection
#test turn directior
def test_turn_left():
    a_car = Rover('name',CompassDirection.NORTH)
    a_car.turn_left()
    assert a_car.direction == CompassDirection.WEST


