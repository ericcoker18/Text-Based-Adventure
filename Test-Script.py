import random

import highMonsClass
import playerClass
import weaponClasses
import lowMonsClass
import eliteMonsClass


#PLAYER CLASS
rceKnight = playerClass.clss("Knight", 135, 20, 3, 5, 25)
rceThief = playerClass.clss("Thief", 80, 40, 5, 2, 50)
rceDuelist = playerClass.clss("Dualist", 100, 50, 8, 1, 40)

pots = 5
playerName = input("Hello adventure, what is your name?\n")
#PLAYER WEAPON
wepSword = weaponClasses.weapon("Sword", 5, 13, 1, 1)
wepAxe = weaponClasses.weapon("Axe", 1, 20, 3, 10)
wepDD = weaponClasses.weapon("Dual Daggers", 3, 7, 1, 3)
wepDDB = weaponClasses.weapon("bad", 0, 1, -10, -50)
#LOW MONSTERS
gbln = lowMonsClass.lowMon('Goblin', 25, 40, 8, 20)
lgbln = lowMonsClass.lowMon('Lesser Goblin', 5, 15, 1, 6)
pxE = lowMonsClass.lowMon('Pixie',10, 40, 10, 20)
imp = lowMonsClass.lowMon('Imp', 4, 20, 3, 5)
wlf = lowMonsClass.lowMon('Wolf', 10, 30, 6, 18)
lowMonsSpawn = [gbln, lgbln, pxE, imp, wlf]
lowMonster = random.choice(lowMonsSpawn)
#HIGH MONSTERS
azazSin = highMonsClass.highMon("Lezaza the Etulosba", 198, 199, 199, 199)
highMonsSpawn = [azazSin]
highMonster = random.choice(highMonsSpawn)
#THE SINS (Values at max until further notice)
luciferPride = eliteMonsClass.eliteMon("Lucifer the prideful Demon", 998, 999, 999, 999)
beelzGluttony = eliteMonsClass.eliteMon("Beelzebub the Gluttonous Ravager", 999, 999, 999, 999)
satanWrath = eliteMonsClass.eliteMon("Satan the Bloodthirsty Knight", 998, 999, 999, 999)
leviEnvy = eliteMonsClass.eliteMon("Leviathan the Vindictive Wretch", 998, 999, 999, 999)
mamGreed = eliteMonsClass.eliteMon("Mammon the Rich & Ruthless King", 998, 999, 999, 999)
belphSloth = eliteMonsClass.eliteMon("Belphegor the Careless", 998, 999, 999, 999)
amodLust = eliteMonsClass.eliteMon("Asmodeus the Lust-full", 998, 999, 999, 999)
azazSin = eliteMonsClass.eliteMon("Azazel the ABSOLUTE", 498, 499, 499, 499)
sinSpawn = [luciferPride, beelzGluttony, satanWrath, leviEnvy, mamGreed, belphSloth, azazSin]
theSin = random.choice(sinSpawn)



racePlayer = input(playerName + " What kind of warrior are you?\n 1. Knight\n 2. Thief\n 3. Dualist\n").lower()

if racePlayer == "knight" or racePlayer == "1":
    playerRace = rceKnight
if racePlayer == "thief" or racePlayer == "2":
    playerRace = rceThief
if racePlayer == "dualist" or racePlayer == "3":
    playerRace = rceDuelist
print("So you're a " + playerRace.name + "!")




print("Hello " + playerName)

weaponChoice = input(playerName + " What weapon would you like to use on your adventure?\n 1. Sword\n 2. Axe\n 3. Dual Daggers\n")

if weaponChoice == "Sword" or weaponChoice == "1":
    chosenWep = wepSword
if weaponChoice == "Axe" or weaponChoice == "2":
    chosenWep = wepAxe
if weaponChoice == "Dual Daggers" or weaponChoice == "3":
    chosenWep = wepDD
print("You chose the " + chosenWep.name)

chosenWep.special = playerRace.splMod
chosenWep.attkMod = playerRace.attkMod
chosenWep.blkMod = playerRace.blkMod


rounds = 1
playerhp = playerRace.health
if playerName.lower() == 'bradley':
    chosenWep = wepDDB
    playerhp = 25
while playerhp > 0:
    normRound = 1
    eliteRound = 2
    bossRound = 3
    shopRound = 4
    if rounds % 10 != 0 and rounds % 3 != 0:
        rnd = 1
    if rounds % 5 == 0 and rounds % 10 != 0:
        rnd = 2
    if rounds % 10 == 0:
        rnd = 3
    if rounds % 3 == 0 and rounds % 10 != 0:
        rnd = 4
    if rnd == normRound:
        currentEnemy = lowMonster
        currentBattleHP = currentEnemy.health()

        print("Enemy " + currentEnemy.name + " has appeared! " + "HP " + str(currentBattleHP))

        while currentBattleHP > 0:
            moveInput = input("What action would you like to take?\n 1. Attack\n 2. Block\n 3. Heal\n").lower()
            if playerhp < 0:
                playerhp = 0
                print("You died! Try Again?")
            if currentBattleHP <= 0:
                currentBattleHP = 0
                print('Victory!')
            if moveInput == "attack" or moveInput == '1':


                monsterAttk = currentEnemy.monAttack()
                attkHit = chosenWep.attack()
                currentBattleHP = currentBattleHP - attkHit
                print(currentEnemy.name + " has " + str(currentBattleHP) + "HP remaining!")
                if currentBattleHP <= 0:
                    currentBattleHP = 0
                else:
                    print(currentEnemy.name + " has attacked for " + str(monsterAttk))
                    playerhp = playerhp - monsterAttk


                print('You have ' + str(playerhp) + 'HP remaining!')
            if moveInput == "block" or moveInput == '2':
                blockVal = chosenWep.block()
                attkVal = currentEnemy.monAttack()
                hitVal = (attkVal - blockVal)
                if attkVal <= 0:
                    print(currentEnemy.name + " Missed!")
                if attkVal > 0:
                    playerhp = playerhp - hitVal
                    print("The " + currentEnemy.name + " Attacked for "+ str(attkVal) + " Damage! \nyou block the enemies attack for " + str(blockVal) + " Damage!\n(you take " + str(hitVal) + " Damage)" "\nYou have " + str(playerhp) + "HP Remaining!")
            if moveInput == "heal" or moveInput == '3':
                if playerhp != playerRace.health:
                    if pots > 0:
                        potionHeal = 20
                        playerhp = potionHeal + playerhp
                        if playerhp > playerRace.health:
                            playerhp = playerRace.health
                        print("Healed! " + str(playerhp) + "Hp Remaining")
                        pots = pots - 1
                        print("Potions Remaining " + str(pots))

                    else:
                        print("You have no potions remaining :(")
                else:
                    print("You are already full HP!")

            if playerhp < 0:
                playerhp = 0
                print("You died! Try Again?")
            if currentBattleHP <= 0:
                currentBattleHP = 0
                print('Victory!')
                rounds = rounds + 1
    if rnd == shopRound:
        upgrade = input("upgrade station\n1. Attack\n2. Block\n3. Special\n").lower()
        if upgrade == "attack" or upgrade == 1:
            playerRace.attkMod = playerRace.attkMod + 1
        if upgrade == "block" or upgrade == 2:
            playerRace.blkMod = playerRace.blkMod + 1
        if upgrade == "special" or upgrade == 3:
            playerRace.splMod = playerRace.splMod + 20
        rounds = rounds + 1
    if rnd == bossRound:
        sinSpawn = [luciferPride, beelzGluttony, satanWrath, leviEnvy, mamGreed, belphSloth, azazSin]
        theSin = random.choice(sinSpawn)
        currentEnemy = theSin
        currentBattleHP = currentEnemy.health()

        print("Enemy " + currentEnemy.name + " has appeared! " + "HP " + str(currentBattleHP))
        while currentBattleHP > 0 and playerhp > 0:
            moveInput = input("What action would you like to take?\n 1. Attack\n 2. Block\n 3. Heal\n").lower()
            if playerhp < 0:
                playerhp = 0
                print("You died! Try Again?")
            if currentBattleHP <= 0:
                currentBattleHP = 0
                print('Victory!')
            if moveInput == "attack" or moveInput == '1':


                monsterAttk = currentEnemy.monAttack()
                attkHit = chosenWep.attack()
                currentBattleHP = currentBattleHP - attkHit
                print(currentEnemy.name + " has " + str(currentBattleHP) + "HP remaining!")
                if currentBattleHP <= 0:
                    currentBattleHP = 0
                else:
                    print(currentEnemy.name + " has attacked for " + str(monsterAttk))
                    playerhp = playerhp - monsterAttk


                print('You have ' + str(playerhp) + 'HP remaining!')
            if moveInput == "block" or moveInput == '2':
                blockVal = chosenWep.block()
                attkVal = currentEnemy.monAttack()
                hitVal = (attkVal - blockVal)
                if attkVal <= 0:
                    print(currentEnemy.name + " Missed!")
                if attkVal > 0:
                    playerhp = playerhp - hitVal
                    print("The " + currentEnemy.name + " Attacked for "+ str(attkVal) + " Damage! \nyou block the enemies attack for " + str(blockVal) + " Damage!\n(you take " + str(hitVal) + " Damage)" "\nYou have " + str(playerhp) + "HP Remaining!")
            if moveInput == "heal" or moveInput == '3':
                if playerhp != playerRace.health:
                    if pots > 0:
                        potionHeal = 20
                        playerhp = potionHeal + playerhp
                        if playerhp > playerRace.health:
                            playerhp = playerRace.health
                        print("Healed! " + str(playerhp) + "Hp Remaining")
                        pots = pots - 1
                        print("Potions Remaining " + str(pots))

                    else:
                        print("You have no potions remaining :(")
                else:
                    print("You are already full HP!")

            if playerhp < 0:
                playerhp = 0
                print("You died! Try Again?")
            if currentBattleHP <= 0:
                currentBattleHP = 0
                print('Victory!')
                rounds = rounds + 1
    if rnd == eliteRound:
        currentEnemy = highMonster
        currentBattleHP = currentEnemy.health()

        print("Enemy " + currentEnemy.name + " has appeared! " + "HP " + str(currentBattleHP))

        while currentBattleHP > 0 and playerhp != 0:
            moveInput = input("What action would you like to take?\n 1. Attack\n 2. Block\n 3. Heal\n").lower()
            if playerhp < 0:
                playerhp = 0
                print("You died! Try Again?")
            if currentBattleHP <= 0:
                currentBattleHP = 0
                print('Victory!')
            if moveInput == "attack" or moveInput == '1':


                monsterAttk = currentEnemy.monAttack()
                attkHit = chosenWep.attack()
                currentBattleHP = currentBattleHP - attkHit
                print(currentEnemy.name + " has " + str(currentBattleHP) + "HP remaining!")
                if currentBattleHP <= 0:
                    currentBattleHP = 0
                else:
                    print(currentEnemy.name + " has attacked for " + str(monsterAttk))
                    playerhp = playerhp - monsterAttk


                print('You have ' + str(playerhp) + 'HP remaining!')
            if moveInput == "block" or moveInput == '2':
                blockVal = chosenWep.block()
                attkVal = currentEnemy.monAttack()
                hitVal = (attkVal - blockVal)
                if attkVal <= 0:
                    print(currentEnemy.name + " Missed!")
                if attkVal > 0:
                    playerhp = playerhp - hitVal
                    print("The " + currentEnemy.name + " Attacked for "+ str(attkVal) + " Damage! \nyou block the enemies attack for " + str(blockVal) + " Damage!\n(you take " + str(hitVal) + " Damage)" "\nYou have " + str(playerhp) + "HP Remaining!")
            if moveInput == "heal" or moveInput == '3':
                if playerhp != playerRace.health:
                    if pots > 0:
                        potionHeal = 20
                        playerhp = potionHeal + playerhp
                        if playerhp > playerRace.health:
                            playerhp = playerRace.health
                        print("Healed! " + str(playerhp) + "Hp Remaining")
                        pots = pots - 1
                        print("Potions Remaining " + str(pots))

                    else:
                        print("You have no potions remaining :(")
                else:
                    print("You are already full HP!")

            if playerhp < 0:
                playerhp = 0
                print("You died! Try Again?")
            if currentBattleHP <= 0:
                currentBattleHP = 0
                print('Victory!')
                rounds = rounds + 1







