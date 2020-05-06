class Person():

    def __init__(self, name):
        self.name = name
        self.health = 20.0
        self.attack = 5
        self.defense = 3
        self.inventory = []

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense