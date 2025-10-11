from src.input_layer.plateau_parser import PlateauParser
import pytest

def test_plateau_parser_parsed_input_value_and_handle_wrong_input():
    parsed =  PlateauParser().parser_plateau_size('2 2')
    except_value = [2,2]
    assert parsed == except_value
    with pytest.raises(TypeError):
        PlateauParser().parser_plateau_size(2)

    with pytest.raises(ValueError):
        PlateauParser().parser_plateau_size('2 is that ok?')