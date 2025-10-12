from src.logic_layer.mission_control import MissionControl
from src.compass_direction import CompassDirection
from src.input_layer.instruction_parser import InstructionParse
from src.input_layer.land_position_parser import LandPositionParser
from src.input_layer.plateau_parser import PlateauParser
# from src.logic_layer.plateau import Plateau
# from src.instruction import Instruction
# import pytest


def test_integration_input_and_mission_control():
    parsed_plateau = PlateauParser().parser_plateau_size('5 5')
    parsed_landposition =  LandPositionParser().parse_land_position('1 2 N')
    parsed_instruction = InstructionParse().parse_instruction('LMLMLMLMM')

    new_mission = MissionControl()
    new_mission.creat_plateau(parsed_plateau)
    new_mission.add_rover(parsed_landposition)
    new_mission.move_latest_rover(parsed_instruction)

    assert new_mission.rovers[next(reversed(new_mission.rovers))].direction == CompassDirection.NORTH
    assert next(reversed(new_mission.rovers))== (1,3)

    parsed_landposition_2 =  LandPositionParser().parse_land_position('3 3 E')
    parsed_instruction_2 = InstructionParse().parse_instruction('MMRMMRMRRM')
    new_mission.add_rover(parsed_landposition_2)
    result = new_mission.move_latest_rover(parsed_instruction_2)
    assert result == [5,1,CompassDirection.EAST]

