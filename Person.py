class Person():

    def __init__(self, name, health, attack, defense, inventory):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory

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

    def getInventroy(self):
        return self.inventory

