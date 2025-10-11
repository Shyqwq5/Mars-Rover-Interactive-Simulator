from src.logic_layer.plateau import Plateau
from src.logic_layer.rover import Rover
from src.instruction import Instruction

class MissionControl:
    def __init__(self):
        self.rovers = {}
        self.plateau = None

    def creat_plateau(self,parsed_plateau):
        new_plateau = Plateau(parsed_plateau[0],parsed_plateau[1])
        self.plateau = new_plateau

    def add_rover(self,parsed_rover):
        if self.rovers:
            number = len(self.rovers)
        else:
            number = 0
        self.add_rover_with_name(f'rover_{number}',parsed_rover)

    def add_rover_with_name(self,name,parsed_rover):
        rover_position = (parsed_rover[0],parsed_rover[1])
        if not self.plateau:
            raise ValueError('no plateau')
        if rover_position not in self.plateau.map:
            raise ValueError('out of plateau')
        if rover_position in self.rovers :
            raise ValueError('The position is not avaliable')
        new_rover = Rover(name,parsed_rover[2])
        self.rovers[rover_position] = new_rover

    def move_latest_rover(self,parsed_instruction):
        if not self.rover:
            raise ValueError('no rover!')

        latest_rover_position = next(reversed(self.rovers))
        latest_rover = self.rovers[latest_rover_position]

        for instruction in parsed_instruction:
            if instruction == Instruction.LEFT:
                latest_rover.turn_left()
            if instruction == Instruction.RIGHT:
                latest_rover.turn_right()
            if instruction == Instruction.MOVE:
                new_position = latest_rover.move(latest_rover_position)
                if new_position in self.rovers:
                    raise ValueError(f'can not keep move! A rover in {new_position}, stay at {latest_rover_position}')
                self.rovers[new_position] = latest_rover
                del self.rovers[latest_rover_position]
                latest_rover_position = new_position











