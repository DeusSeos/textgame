class Mob():

    def __init__(self, name = '', health = 0.0, attack = 0.0, defense = 0.0):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return "{}||{}||{}||{}".format(self.name, self.health, self.attack, self.defense)

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

