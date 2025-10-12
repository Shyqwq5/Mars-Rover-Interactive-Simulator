import random

class Plateau:
    def __init__(self,latitude:str,lontitude:str):
        self.latitdude =latitude
        self.lontitude = lontitude
        self.map = self.creat_map()

    def creat_map(self):
        map = {}
        for i in range(self.latitdude+1):
            for j in range(self.lontitude+1):
                map[(i,j)] = None
        return map

    def creat_rough_map(self,percentage = 0.1):
        map = {}
        for i in range(self.latitdude+1):
            for j in range(self.lontitude+1):
                if random.random() < percentage:
                    map[(i,j)] = 'rocket'
                else:
                    map[(i,j)] = None

