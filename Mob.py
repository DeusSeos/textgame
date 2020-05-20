class Mob():

    def __init__(self, name='No Mob', health=0.0, attack=0.0, defense=0.0):
        self.maxHealth = 150.0
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

    def damage(self, dmg):
        self.health -= dmg
        if self.health < 0:
            self.health = 0.0
        return None
    
    def heal(self, newHealth):
        self.health  += newHealth
        if self.health > self.maxHealth:
            self.health = 100.0
        return None

    def isAlive(self):
        return self.health > 0.0
