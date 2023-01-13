import random

class clss:
    def __init__(self, name, health, mana, attkMod, blkMod, splMod):
        self.name = name
        self.health = health
        self.mana = mana
        self.attkMod = attkMod
        self.blkMod = blkMod
        self.splMod = splMod


    def __str__(self):
        return self.name

    def special(self):
        spcl = self.splMod
        return spcl