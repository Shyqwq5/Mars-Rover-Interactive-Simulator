from src.logic_layer.mission_control import MissionControl
from src.compass_direction import CompassDirection
from src.input_layer.instruction_parser import InstructionParse
from src.input_layer.land_position_parser import LandPositionParser
from src.input_layer.plateau_parser import PlateauParser

from tqdm import tqdm
import time






for i in tqdm(range(100), desc="Processing"):
    time.sleep(0.01)

created = False
while not created:
    try:
        plateau_size_input = input("Set the plateau size, e.g., 5 5: ")
        parsed_plateau = PlateauParser().parser_plateau_size(plateau_size_input)
        new_mission = MissionControl()
        new_mission.creat_plateau(parsed_plateau)
        new_mission.print_map()
        created = True
    except ValueError as e:
        print(e)


landed = False
while not landed:
    try:
        land_position_input = input("Enter the rover landing position and direction, e.g., 1 2 N: ")
        parsed_landposition =  LandPositionParser().parse_land_position(land_position_input)
        new_mission.add_rover(parsed_landposition)
        new_mission.print_map()
        landed = True
    except ValueError as e:
        print(e)

moved = False

while not moved:
    try:
        instruction_input = input("Enter the instruction for rover, e.g., LMLMLMLMM: ")
        parsed_instruction = InstructionParse().parse_instruction(instruction_input)
        new_mission.move_latest_rover(parsed_instruction)
        new_mission.print_map()
        moved = True
    except ValueError as e:
        print(e)
        new_mission.print_map()
