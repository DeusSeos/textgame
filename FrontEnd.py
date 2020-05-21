from Backend import *
from UI import *
import random


class FrontEnd():
    def __init__(self):
        return None

    def attackPerson(self, Person, Mob):
        dmg = (Mob.getAttack()/Person.getDefense())
        Person.damage(dmg=dmg)
        return dmg

    def attackMob(self, Person, Mob):
        #print(Person.getAttack())
        #print(Mob.getDefense())
        dmg = (Person.getAttack()/Mob.getDefense())
        Mob.damage(dmg = dmg)
        return dmg

    def healPerson(self, Person, hr = 2):
         Person.heal(hr)
         return hr

    def healMob(self, Mob, hr = 1):
        Mob.heal(hr)
        return hr

    def attackSequence(self, Person, Mob, Location, Backend):
        if Mob.isAlive():
            dmg = FrontEnd.attackMob(self, Person, Mob)
            mobName = Mob.getName()
            if random.randrange(0, 10) > 7:
                mobAction = 'healed'
                mobI = FrontEnd.healMob(self, Mob = Mob)
            else:
                mobAction = "attacked"
                mobI = FrontEnd.attackPerson(self, Person, Mob)
            message = "You have attacked {} for {} damage.\n{} has {} for {}".format(mobName, dmg, mobName, mobAction,mobI)
        else:
            if (Location.getMobs() != []):
                message = "You have killed a {}".format(Mob.getName())
                print(Location.getMobs())
                Location.removeMob(Mob)
                Backend.setCurrentMob()
                if (Location.getMobs() == []):
                    Person.increaseAttack()
                    Person.increaseDefense()
                    message = "You have freed this city.\nYour attack has gone up by 1!\nYour defense has gone up by .5!"
            else:
                message = "Let's move on to the next city."

        self.updateActionInfoBar(message)

    def healSequence(self, Person, Mob):
        #dmg = FrontEnd.attackPerson(self, Person, Mob)
        heal = FrontEnd.healPerson(self, Person)
        mobName = Mob.getName()
        if random.randrange(0, 10) > 7:
            mobAction = 'healed'
            mobI = FrontEnd.healMob(self, Mob = Mob)
        else:
            mobAction = "attacked"
            mobI = FrontEnd.attackPerson(self, Person, Mob)
        message = "You have healed for {}.\n{} has {} for {}".format(heal, mobName, mobAction,mobI)
        self.updateActionInfoBar(message)

    def newGame(self, Backend):
        Backend.initializeGame()
        self.updateActionInfoBar("Use the attack and heal buttons to kill the monsters!")