class Mob():

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

