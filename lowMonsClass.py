import random
class lowMon:
    def __init__(self, name, HPmin, HPmax, monDMGmin, monDMGmax):
        self.name = name
        self.monHPmin = HPmin
        self.monHPmax = HPmax
        self.monDMGmin = monDMGmin
        self.monDMGmax = monDMGmax


    def __str__(self):
        return self.name

    def health(self):
        monsterHealth = random.randint(self.monHPmin, self.monHPmax)
        return monsterHealth
    def monAttack(self):
        monsterAttack = random.randint(self.monDMGmin, self.monDMGmax)
        return monsterAttack