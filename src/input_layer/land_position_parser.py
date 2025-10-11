from src.compass_direction import CompassDirection

class LandPositionParser:
    def __init__(self):
        pass
    def parse_land_position(self,input_str):
        if not isinstance(input_str,str):
            raise TypeError('not a string!')
        try:
            parsed_list = []
            input_list = input_str.split()
            parsed_list.append(int(input_list[0]))
            parsed_list.append(int(input_list[1]))
            valied_character={'N':CompassDirection.NORTH,'W':CompassDirection.WEST,'S':CompassDirection.SOUTH,'E':CompassDirection.EAST}
            parsed_list.append(valied_character[(input_list[2])])
            return parsed_list
        except:
            raise ValueError('not a vaild input.')


