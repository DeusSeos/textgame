

class FrontEnd():
    def __init__(self):
        return None

    def attackPerson(self, Person, Mob):
        dmg = (Mob.getAttack()/Person.getDefense())
        Person.damage(dmg=dmg)

    def attackMob(self, Person, Mob):
        #print(Person.getAttack())
        #print(Mob.getDefense())
        dmg = (Person.getAttack()/Mob.getDefense())
        Mob.damage(dmg = dmg)

    def healPerson(self, Person, hr = 2):
         Person.heal(hr)

