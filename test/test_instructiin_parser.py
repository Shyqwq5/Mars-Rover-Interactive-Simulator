from src.input_layer.instruction_parser import InstructionParse
import pytest
from src.instruction import Instruction
def test_instruction_parse_input_into_enum_object_list():
    parsed  = InstructionParse().parse_instruction('L')
    except_result = [Instruction.LEFT]
    assert parsed == except_result
    with pytest.raises(TypeError):
        InstructionParse().parse_instruction(666)
    with pytest.raises(ValueError):
        InstructionParse().parse_instruction('hahahhaha')