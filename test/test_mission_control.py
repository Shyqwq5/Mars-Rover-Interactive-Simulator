from src.logic_layer.mission_control import MissionControl
from src.logic_layer.plateau import Plateau
from src.instruction import Instruction
from src.compass_direction import CompassDirection
import pytest

def test_mission_control_can_creat_plateau():
    new_mission = MissionControl()
    new_mission.creat_plateau([9,9])
    assert new_mission.plateau.map == Plateau(9,9).map

def test_mission_control_can_add_rover():
    new_mission = MissionControl()
    new_mission.creat_plateau([9,9])
    new_mission.add_rover([1,2,CompassDirection.NORTH])
    assert new_mission.rovers[next(reversed(new_mission.rovers))].direction  == CompassDirection.NORTH
    new_mission.add_rover([6,6,CompassDirection.SOUTH])
    assert new_mission.rovers[next(reversed(new_mission.rovers))].direction == CompassDirection.SOUTH
    assert new_mission.rovers[next(reversed(new_mission.rovers))].name == 'rover_1'

def test_mission_control_add_rover_error_control():
    with pytest.raises(ValueError):
        new_mission = MissionControl()
        new_mission.add_rover([1,2,CompassDirection.NORTH])
    with pytest.raises(ValueError):
        new_mission = MissionControl()
        new_mission.creat_plateau([9,9])
        new_mission.add_rover([10,2,CompassDirection.NORTH])

def test_mission_control_can_move_rover():
    new_mission = MissionControl()
    new_mission.creat_plateau([9,9])
    new_mission.add_rover([1,2,CompassDirection.NORTH])
    new_mission.move_latest_rover([Instruction.LEFT])
    assert new_mission.rovers[next(reversed(new_mission.rovers))].direction == CompassDirection.WEST
    new_mission.move_latest_rover([Instruction.RIGHT])
    assert new_mission.rovers[next(reversed(new_mission.rovers))].direction == CompassDirection.NORTH
    new_mission.move_latest_rover([Instruction.RIGHT,Instruction.LEFT,Instruction.RIGHT,Instruction.MOVE])
    assert new_mission.rovers[next(reversed(new_mission.rovers))].direction == CompassDirection.EAST
    assert next(reversed(new_mission.rovers))== (2,2)












