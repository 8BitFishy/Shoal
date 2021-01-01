import random
from itertools import count

class Actors:
    _ids = count(0)

    def __init__(self,  startingvectors, angles, speed):
        self.id = next(self._ids)
        self.vectors = startingvectors
        self.angles = angles
        self.speed = speed


actorlist = []

def Generate_Actors(actorcount):
    for i in range(actorcount):
        speed = 10
        startingvectors = [[0, 0, 0]]
        angles = [[0, 0, 0]]
        for j in range(3):
            startingvectors[0][j] = random.randint(20, 40)
        Actor = Actors(startingvectors, angles, speed)
        actorlist.append(Actor)

    return actorlist