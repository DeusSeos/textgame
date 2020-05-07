class Mob():

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return "{}||{}||{}||{}||{}".format(self.name, self.health, self.attack, self.defense, self.inventory)

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

