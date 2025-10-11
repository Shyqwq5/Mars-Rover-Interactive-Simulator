from src.input_layer.land_position_parser import LandPositionParser
from src.compass_direction import CompassDirection
import pytest

def test_land_position_parser():
    parserd = LandPositionParser().parse_land_position('1 2 N')
    excepted_output = [1,2,CompassDirection.NORTH]
    assert parserd == excepted_output

    with pytest.raises(TypeError):
        LandPositionParser().parse_land_position([1111])
    with pytest.raises(ValueError):
        LandPositionParser().parse_land_position('1 2 3')