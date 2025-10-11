class PlateauParser:
    def __init__(self):
        pass
    def parser_plateau_size(self,size_str):
        if not isinstance(size_str,str):
            raise TypeError('not a string!')
        try:
            size_lsit = size_str.split()
            return [int(chara) for chara in size_lsit]
        except:
            raise ValueError('not a vaild input.')




