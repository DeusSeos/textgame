# This is the driving code for creating the different objects
# Special characters to indicate end of a section and end of a location
# End of location: ***
#
from Location import *
from Person import *
from Mob import *


class Backend():
    def __init__(self):
        self.locationArray = []
        self.personArray = []
        self.mobArray = []
        self.currentLocation = Location()
        self.currentMob = Mob()

    def initializeLocations(self, fileName='Location.txt'):
        wordsRemove = ['Location:', 'Welcome Message:', 'Objects:', 'Connecting Locations:', 'Mobs:']
        readDataList = []
        locations = []
        locationTotal = 0

        try:  # checks to see if file exists or not
            with open(fileName) as fileInit:
                if (fileInit.read() == ''):
                    print('File exists but is empty. Will append structure to file')
                else:
                    print("File exists. Structure hasn't been checked.")
        except:
            print("File doesn't exist ")
            fileInit = open(fileName, 'w+')
            fileInit.write("Location:\nWelcome Message:\nObjects:\nConnecting Locations:\nMobs:\n***\n")
            fileInit.close()
        with open(fileName) as file:
            for line in file:
                readDataList.append(line.replace('\n', '').strip())
        for index, element in enumerate(
                readDataList):  # check total location and cleaning up the location syntax before stuffing into array
            if element == '***':
                locationTotal += 1
            for word in wordsRemove:
                if word in element:
                    readDataList[index] = element.replace(word, '')
                    break
        index = 0
        i = 0
        while i < locationTotal:
            location = readDataList[index].strip()
            welcomeMessage = readDataList[index + 1].strip()
            objects = readDataList[index + 2].strip().split(',')
            connectingLocations = readDataList[index + 3].strip().split(',')
            mobs = readDataList[index + 4].strip().split(',')
            locationMobs = []
            for mob in self.mobArray:  # looping through mobArray type object
                for mobName in mobs:  # looping thru mob Name
                    if mob.getName() == mobName:
                        locationMobs.append(mob)
            # for mob in locationMobs: #checking locationMobs is initializing correctly
            #     print(mob)
            a = Location.Location(location, welcomeMessage, objects, connectingLocations, locationMobs)
            locations.append(a)
            index += 6
            i += 1

        return locations

    def initializePerson(self, fileName='Person.txt'):
        wordsRemove = ["Name:", "Health:", "Attack:", "Defense:", "Inventory:", "Location:", "***"]
        readDataList = []
        persons = []
        personsTotal = 0

        try:  # checks to see if file exists or not
            with open(fileName) as fileInit:
                if (fileInit.read() == ''):
                    print('File exists but is empty. Will append structure to file')
                else:
                    print("File exists. Structure hasn't been checked.")
        except:
            print("File doesn't exist ")
            fileInit = open(fileName, 'w+')
            fileInit.write("Name:\nHealth:\nAttack:\nDefense:\nInventory:\nLocation:\n***\n")
            fileInit.close()
        with open(fileName) as file:
            for line in file:
                readDataList.append(line.replace('\n', '').strip())
        for index, element in enumerate(
                readDataList):  # check total persons and cleaning up the person syntax before stuffing into array
            if element == '***':
                personsTotal += 1
            for word in wordsRemove:
                if word in element:
                    readDataList[index] = element.replace(word, '')
                    break

        index = 0
        i = 0

        while i < personsTotal:
            name = readDataList[index].strip()
            health = float(readDataList[index + 1].strip())
            attack = float(readDataList[index + 2].strip())
            defense = float(readDataList[index + 3].strip())
            inventory = readDataList[index + 4].strip().split(',')
            location = readDataList[index + 5].strip()
            a = Person.Person(name, health, attack, defense, inventory, location)
            persons.append(a)
            index += 6
            i += 1

        return persons

    def initializeMobs(self, fileName='Mob.txt'):
        wordsRemove = ["Name:", "Health:", "Attack:", "Defense:", "***"]
        readDataList = []
        mobs = []
        mobsTotal = 0
        try:  # checks to see if file exists or not
            with open(fileName) as fileInit:
                if (fileInit.read() == ''):
                    print('File exists but is empty. Will append structure to file')
                    fileInit.write("Name:\nHealth:\nAttack:\nDefense:\n***\n")
                else:
                    print("File exists. Structure hasn't been checked.")
        except:
            print("File doesn't exist ")
            with open(fileName, 'w+') as fileInit:
                fileInit.write("Name:\nHealth:\nAttack:\nDefense:\n***\n")
        with open(fileName) as file:
            for line in file:
                readDataList.append(line.replace('\n', '').strip())
        for index, element in enumerate(
                readDataList):  # check total mobs and cleaning up the location syntax before stuffing into array
            if element == '***':
                mobsTotal += 1
            for word in wordsRemove:
                if word in element:
                    readDataList[index] = element.replace(word, '')
                    break

        index = 0
        i = 0
        while i < mobsTotal:
            name = readDataList[index].strip()
            health = float(readDataList[index + 1].strip())
            attack = float(readDataList[index + 2].strip())
            defense = float(readDataList[index + 3].strip())
            a = Mob.Mob(name, health, attack, defense)
            mobs.append(a)
            index += 5
            i += 1

        return mobs

    def save(self, locationName='SaveLocation.txt', personName='SavePerson.txt', mobName='SaveMob.txt', currentName='Current.txt'):  # dumps all objects from the arrays into yaml files for save states
        # self.locationArray
        # self.personArray
        # self.mobArray
        # print(self.locationArray)
        # print(self.personArray)
        # print(self.mobArray)
        print("Saving...")
        with open(locationName, "w+") as file:
            for location in self.locationArray:
                name = location.getLocation()
                message = location.getWelcomeMessage()
                obj = ','.join(location.getObjects())
                connectLoc = ','.join(location.getConnectingLocations())
                mobs = []
                for mob in location.getMobs():
                    mobs.append(mob.getName())
                mobs = ",".join(mobs)
                section = "Location: {}\nWelcome Message: {}\nObjects: {}\nConnecting Locations: {}\nMobs: {}\n***\n".format(
                    name, message, obj, connectLoc, mobs)
                file.write(section)
        with open(personName, "w+") as file:
            for person in self.personArray:
                name = person.getName()
                health = person.getHealth()
                attack = person.getAttack()
                defense = person.getDefense()
                inventory = ','.join(person.getInventory())
                location = person.getLocation()
                section = "Name: {}\nHealth: {}\nAttack: {}\nDefense: {}\nInventory: {}\nLocation: {}\n***\n".format(
                    name, health, attack, defense, inventory, location)
                file.write(section)
        with open(mobName, "w+") as file:
            for mob in self.mobArray:
                name = mob.getName()
                health = mob.getHealth()
                attack = mob.getAttack()
                defense = mob.getDefense()
                section = "Name: {}\nHealth: {}\nAttack: {}\nDefense: {}\n***\n".format(name, health, attack, defense)
                file.write(section)
        with open(currentName, "w+") as file:
            locname = self.getCurrentLocation().getLocation()
            mobname = self.getCurrentMob().getName()


            section = "Location: {}\n Mobs: {}\n***\n".format(locname, mobname)
            file.write(section)

    def load(self):
        self.locationArray = []
        self.personArray = []
        self.mobArray = []
        print("Loading...")
        self.locationArray = self.initializeLocations("SaveLocation.txt")
        self.personArray = self.initializePerson("SavePerson.txt")
        self.mobArray = self.initializeMobs("SaveMob.txt")

    def initializeGame(self):
        self.locationArray = []
        self.personArray = []
        self.mobArray = []
        self.mobArray = self.initializeMobs()
        self.locationArray = self.initializeLocations()
        self.personArray = self.initializePerson()

    def getLocationArray(self):
        return self.locationArray

    def getPersonArray(self):
        return self.personArray

    def getMobArray(self):
        return self.mobArray

    def getCurrentLocation(self):
        return self.currentLocation

    def setCurrentLocation(self, locationName=''):
        for loc in self.locationArray():
            if locationName == loc.getLocation():
                self.currentLocation = loc

        return None

    def getCurrentMob(self):
        return self.currentMob

    def setCurrentMob(self, mobName=''):
        loc = self.getCurrentLocation()
        mobs = loc.getMobs()
        for mob in mobs:
            if mobName == mob.getName():
                self.mob = mob
                break
        return None
