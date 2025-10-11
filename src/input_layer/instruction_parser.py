from src.instruction import Instruction

class InstructionParse:
    def __init__(self):
        pass

    def parse_instruction(self,instruction_str):

        if not isinstance(instruction_str,str):
            raise TypeError('not a string!')

        vaild_character = {'L':Instruction.LEFT,'R':Instruction.RIGHT,'M':Instruction.MOVE}
        parsed_instruction  = []

        for character in  instruction_str:
            if character in vaild_character:
                parsed_instruction.append(vaild_character[character])
            else:
                raise ValueError('not vaild input.')

        return parsed_instruction





