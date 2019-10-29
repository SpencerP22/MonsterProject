import random


class Monster:
    def __init__(self, name):
        self.health = 30
        self.name = name

    def getHealth(self):
        return self.health

    def getName(self):
        return self.name

    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

    def isAlive(self):
        if self.health > 0:
            return True
        return False

    def attack(self):
        damage = random.random() * 10 // 1
        return damage


class ArmoredMonster(Monster):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 30

    def getArmor(self):
        return self.armor

    def takeDamage(self, damage):
        if self.armor > 0:
            if damage > self.armor:
                damageLeft = damage - self.armor
                self.armor = 0
                self.health = self.health - damageLeft
                if self.health < 0:
                    self.health = 0
            else:
                self.armor = self.armor - damage
        else:
            self.health = self.health - damage
            if self.health < 0:
                self.health = 0


def battle(Monster1, Monster2):
    round = 1
    while Monster1.isAlive() and Monster2.isAlive():
        print("------- Round: " + str(round) + " -------")
        printStats(Monster1, Monster2)
        #each monster attacks
        mon1damage = Monster1.attack()
        mon2damage = Monster2.attack()
        Monster2.takeDamage(mon1damage)
        Monster1.takeDamage(mon2damage)

        print(Monster2.getName() + " attacks and deals " + str(mon2damage) + " damage!")
        print(Monster1.getName() + " attacks and deals " + str(mon1damage) + " damage!\n")
        round += 1
    if not Monster1.isAlive() and not Monster2.isAlive():
        print("It's a draw!")
    elif not Monster1.isAlive():
        print(Monster2.getName() + " Wins!")
    else:
        print(Monster1.getName() + " Wins!")


def printStats(*monsters):
    for monster in monsters:
        statstring = ""
        statstring += monster.getName() + " ---"
        if isinstance(monster, ArmoredMonster):
            statstring += " Armor: " + str(monster.getArmor()) + "\n" + " " * len(statstring)
        statstring += " Health: " + str(monster.getHealth()) + "\n--------------------------"
        print(statstring)


def main():
    gargazhoul = ArmoredMonster("Gargazhoul")
    azazel = ArmoredMonster("Azazel")
    #printStats(azazel)
    mon = Monster("bleh")
    #printStats(mon)
    battle(gargazhoul, azazel)


main()
