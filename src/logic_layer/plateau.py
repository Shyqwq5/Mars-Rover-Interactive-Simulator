class Plateau:
    def __init__(self,latitude:str,lontitude:str):
        self.latitdude =latitude
        self.lontitude = lontitude
        self.map = self.creat_map()

    def creat_map(self):
        map = set()
        for i in range(self.latitdude+1):
            for j in range(self.lontitude+1):
                map.add((i,j))
        return map

