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
        # self.personArray = []
        self.mobArray = []
        self.currentLocation = Location()
        self.currentMob = Mob()
        self.currentPerson = Person()

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
            # print(mobs)
            # print(self.mobArray)
            for mob in self.mobArray:  # looping through mobArray type object
                # print("first loop" + mob.getName())
                for mobName in mobs:  # looping thru mob Name
                    # print("second loop "+ mobName)
                    if mob.getName() == mobName:
                        locationMobs.append(mob)
            # print(locationMobs)
            # for mob in locationMobs: #checking locationMobs is initializing correctly
            #     print(mob)
            a = Location(location, welcomeMessage, objects, connectingLocations, locationMobs)
            locations.append(a)
            index += 6
            i += 1

        return locations

    def initializePerson(self, fileName='Person.txt'):
        wordsRemove = ["Name:", "Health:", "Attack:", "Defense:", "Inventory:", "Location:", "***"]
        readDataList = []

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
        name = readDataList[index].strip()
        health = float(readDataList[index + 1].strip())
        attack = float(readDataList[index + 2].strip())
        defense = float(readDataList[index + 3].strip())
        inventory = readDataList[index + 4].strip().split(',')
        location = readDataList[index + 5].strip()
        a = Person(name, health, attack, defense, inventory, location)
        self.setCurrentLocation()
        self.setCurrentMob()
        self.currentPerson = a

        return a

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
            a = Mob(name, health, attack, defense)
            mobs.append(a)
            index += 5
            i += 1

        return mobs

    def save(self, locationName='SaveLocation.txt', personName='SavePerson.txt', mobName='SaveMob.txt',
             currentName='SaveCurrent.txt'):  # dumps all objects from the arrays into yaml files for save states
        # self.locationArray
        # self.personArray
        # self.mobArray
        # print(self.locationArray)
        # print(self.personArray)
        # print(self.mobArray)
        print("Saving...")
        with open(locationName, "w+") as file:
            for location in self.locationArray:
                name = location.getName()
                message = location.getWelcomeMessage()
                obj = ','.join(location.getObjects())
                connectLoc = ','.join(location.getConnectingLocations())
                mobArray = []
                for mob in location.getMobs():
                    if mob.isAlive():
                        mobArray.append(mob.getName())
                print(mobArray)
                mobs = ",".join(mobArray)
                print(mobs)
                section = "Location: {}\nWelcome Message: {}\nObjects: {}\nConnecting Locations: {}\nMobs: {}\n***\n".format(name, message, obj, connectLoc, mobs)
                file.write(section)
        with open(personName, "w+") as file:
            name = self.currentPerson.getName()
            health = self.currentPerson.getHealth()
            attack = self.currentPerson.getAttack()
            defense = self.currentPerson.getDefense()
            inventory = ','.join(self.currentPerson.getInventory())
            location = self.currentPerson.getLocation()
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
            locname = self.getCurrentLocation().getName()
            mobname = self.getCurrentMob().getName()
            # print(locname)
            # print(mobname)
            section = "Location: {}\nMobs: {}\n***\n".format(locname, mobname)
            file.write(section)

    def load(self, currentName='SaveCurrent.txt'):
        wordsRemove = ['Location:', 'Mobs:']
        self.locationArray = []
        # self.personArray = []
        self.mobArray = []
        readDataList = []
        print("Loading...")
        self.mobArray = self.initializeMobs("Mob.txt")
        self.locationArray = self.initializeLocations("SaveLocation.txt")
        self.currentPerson = self.initializePerson("SavePerson.txt")
        with open(currentName, "r") as file:
            for line in file:
                readDataList.append(line.replace('\n', '').strip())
        for index, element in enumerate(
                readDataList):  # check total location and cleaning up the location syntax before stuffing into array
            for word in wordsRemove:
                if word in element:
                    readDataList[index] = element.replace(word, '').strip()
                    break
        currentLocationName = readDataList[0]
        currentMobName = readDataList[1]
        for location in self.getLocationArray():
            if location.getName() == currentLocationName:
                self.currentLocation = location
        # print('currentMobname' +currentMobName)
        for mob in self.getMobArray():
            # print(mob.getName())
            if mob.getName() == currentMobName:
                self.currentMob = mob

    def initializeGame(self):
        self.locationArray = []
        # self.personArray = []
        self.mobArray = []
        self.mobArray = self.initializeMobs()
        self.locationArray = self.initializeLocations()
        self.currentPerson = self.initializePerson()
        for loc in self.locationArray:
            if loc.getName() == self.currentPerson.getLocation():
                self.currentLocation = loc
        self.currentMob = self.currentLocation.getMobs()[0]


    def getLocationArray(self):
        return self.locationArray

    def getPerson(self):
        return self.currentPerson

    def getMobArray(self):
        return self.mobArray

    def getCurrentLocation(self):
        return self.currentLocation

    def setCurrentLocation(self, locationName=''):
        for loc in self.locationArray:
            if self.currentPerson.getLocation() == loc.getName():
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
        return self.currentMob

    def moveTo(self):
        # print(self.getCurrentLocation().getConnectingLocations())
        nextLoc = self.currentLocation.getConnectingLocations()[0]

        for loc in self.getLocationArray():
            # print(loc)
            if nextLoc == loc.getName():
                # print(loc.getMobs())
                self.mobs = loc.getMobs()
                self.currentMob = self.mobs[0]
                self.currentLocation = loc
                self.currentPerson.setLocation(nextLoc)


