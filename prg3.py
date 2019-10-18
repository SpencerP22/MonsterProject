class Monster:
    def __init__(self):
        self.health = 30

    def getHealth(self):
        return self.health
    
    def takeDamage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        return self.health


def main():
    mon = Monster()
    print(mon.getHealth())

    print(mon.getHealth())



main()
