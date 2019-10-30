import random

"""
    Spencer Palmeter - Monster Project
    additional changes:
        - added monster naming and default values
        - added basic battle functionality between two monsters. Round based
          fighting, Monster A attacks Monster B and vice versa until one
          Monster's health reaches 0
            - added RNG based attacks for battling
            - added variable argument printout for displaying 
              current health and armor for x monsters that displays 
              after each round
"""


class Monster:
    # Default Monster constructor
    def __init__(self, name="Evil Spirit", health=30):
        self.health = health
        self.name = name

    def getHealth(self):
        return self.health

    def getName(self):
        return self.name

    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0

    # Health check
    def isAlive(self):
        if self.health > 0:
            return True
        return False

    # RNG based damage output
    def attack(self):
        damage = random.random() * 10 // 1
        return damage


class ArmoredMonster(Monster):
    # Default ArmoredMonster constructor
    def __init__(self, name="Spectral Knight", health=30, armor=30):
        super().__init__(name, health)
        self.armor = armor

    def getArmor(self):
        return self.armor

    # ArmoredMonster takes damage from its armor value first, once that is reduced to 0
    # the remaining damage is subtracted from health
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


# Simulates a battle between two monsters. Each monster attacks until one's health reaches 0
def battle(Monster1, Monster2):
    round = 1
    while Monster1.isAlive() and Monster2.isAlive():
        print("------- Round: " + str(round) + " -------")
        printStats(Monster1, Monster2)
        # each monster attacks
        mon1damage = Monster1.attack()
        mon2damage = Monster2.attack()
        Monster2.takeDamage(mon1damage)
        Monster1.takeDamage(mon2damage)
        # attack message
        print(Monster2.getName() + " attacks and deals " + str(mon2damage) + " damage!")
        print(Monster1.getName() + " attacks and deals " + str(mon1damage) + " damage!\n")
        round += 1
    # end of round health check
    if not Monster1.isAlive() and not Monster2.isAlive():
        print("It's a draw!")
    elif not Monster1.isAlive():
        print(Monster2.getName() + " Wins!")
    else:
        print(Monster1.getName() + " Wins!")


# prints health and armor(if applicable) stats for x amount of Monsters
def printStats(*monsters):
    for monster in monsters:
        statstring = ""
        statstring += monster.getName() + " ---"
        if isinstance(monster, ArmoredMonster):
            statstring += " Armor: " + str(monster.getArmor()) + "\n" + " " * len(statstring)
        statstring += " Health: " + str(monster.getHealth()) + "\n--------------------------"
        print(statstring)


def main():
    malphas = ArmoredMonster("Malphas", 35, 40)
    azazel = ArmoredMonster("Azazel", 40, 25)
    battle(malphas, azazel)


main()
