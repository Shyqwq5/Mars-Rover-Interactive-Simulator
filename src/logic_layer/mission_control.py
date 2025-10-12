from src.logic_layer.plateau import Plateau
from src.logic_layer.rover import Rover
from src.instruction import Instruction
from src.compass_direction import CompassDirection
import time


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
        if self.plateau.map[rover_position] != None:
            raise ValueError(f'got {self.plateau.map[rover_position]} in {rover_position}')
        if rover_position in self.rovers :
            raise ValueError('The position is not avaliable')
        new_rover = Rover(name,parsed_rover[2])
        self.rovers[rover_position] = new_rover

    def move_latest_rover(self,parsed_instruction):
        if not self.rovers:
            raise ValueError('no rover!')

        latest_rover_position = next(reversed(self.rovers))

        return self.move_a_rover_with_position(latest_rover_position,parsed_instruction)


    def move_a_rover_with_name(self,name,parsed_instruction):

        if not self.rovers:
            raise ValueError('no rover!')

        for key,value in self.rovers.items:
            if value.name == name:
                return self.move_a_rover_with_position(key,parsed_instruction)
            else:
                raise ValueError(f'no rover named {name}')



    def move_a_rover_with_position(self,position,parsed_instruction):
        if not self.rovers:
                raise ValueError('no rover!')
        try:
            rover = self.rovers[position]
        except:
            raise ValueError(f'no rover in position {position}')

        for instruction in parsed_instruction:
            if instruction == Instruction.LEFT:
                rover.turn_left()
            if instruction == Instruction.RIGHT:
                rover.turn_right()
            if instruction == Instruction.MOVE:
                new_position = rover.move(position)
                if new_position in self.rovers:
                    raise ValueError(f'can not keep move! A rover in {new_position}, stay at {position}')
                if new_position not in self.plateau.map:
                    raise ValueError(f'can not keep move! At the edge of plateau, stay at {position}')
                if self.plateau.map[new_position] != None:
                    raise ValueError(f'got {self.plateau.map[new_position]} in {new_position}')
                self.rovers[new_position] = rover
                del self.rovers[position]
                position = new_position

        return [position[0],position[1],rover.direction]

    def print_map(self):

        symbols = {
        CompassDirection.EAST:"▸",
        CompassDirection.NORTH:"▴",
        CompassDirection.WEST:"◂",
        CompassDirection.SOUTH:"▾",
        'rocket':"◼",
        None:'●'
        }

        for j in range(self.plateau.latitdude,-1,-1):
            for i in range(0,self.plateau.lontitude+1):
                if (i,j) in self.rovers:
                    symbol = symbols[self.rovers[(i,j)].direction] + ' '
                else:
                    symbol = symbols[self.plateau.map[(i,j)]] + ' '
                if i == self.plateau.lontitude:
                    print(symbol)
                else:
                    print(symbol,end="")



