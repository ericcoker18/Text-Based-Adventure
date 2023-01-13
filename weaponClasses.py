import random
import playerClass
class weapon:
    def __init__(self, name, dmgMin, dmgMax, minBlock, maxBlock, blkMod = 0, attkMod = 0, special = 0):
        self.name = name
        self.dmgMin = dmgMin
        self.dmgMax = dmgMax
        self.minBlock = minBlock
        self.maxBlock = maxBlock
        self.special = special
        self.blkMod = blkMod
        self.attkMod = attkMod

    def __str__(self):
        return self.name

    def attack(self):
        playerDmg = random.randint(self.dmgMin, self.dmgMax) + self.attkMod
        if self.name == "Dual Daggers":
            print("Your first attack hit for " + str(playerDmg) + " Damage!")
            extraDmg = int(random.randint(1, 4) + self.special / 10)
            print("Your second attack hit for " + str(extraDmg) + " Damage!")
            playerDmg = playerDmg + extraDmg
        else:
            print("Your attack hit for " + str(playerDmg) + " Damage!")
        return playerDmg
    def block(self):
        blockDMG = random.randint(self.minBlock, self.maxBlock) + self.blkMod
        return blockDMG
    def heal(self):
        if pots > 0:
            potionHeal = 20
            playerhp=100
            playerhp = potionHeal + playerhp
            print("Healed!")
            return playerhp
        else:
            print("You have no potions remaining :(")

