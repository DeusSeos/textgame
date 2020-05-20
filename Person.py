class Person():

    def __init__(self, name= '', health = 0.0, attack = 0.0, defense = 0.0, inventory = [], location = 'Ragni'):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
        self.location = location
        self.maxHealth = 100

    def __str__(self):
        return "{}||{}||{}||{}||{}".format(self.name, self.health, self.attack, self.defense, self.inventory)

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def damage(self, dmg):
        self.health -= dmg
        return None

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getInventory(self):
        return self.inventory

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation = ''):
        self.location = newLocation

    def setName(self, newName):
        self.name = newName
        return None

    def heal(self, newHealth):
        self.health  += newHealth
        if self.health > self.maxHealth:
            self.health = 100.0
        return None




