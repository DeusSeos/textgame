# This is the driving code for creating the different objects
# Special characters to indicate end of a section and end of a location
# End of location: ***
#

import Location
import Mob
import Person
import yaml

locationArray = []
personArray = []
mobArray = []

def initializeLocations(fileName = 'Location.txt'):
    wordsRemove = ['Location:', 'Welcome Message:', 'Objects:', 'Connecting Locations:', 'Mobs:']
    readDataList = []
    locations = []
    locationTotal = 0

    try: #checks to see if file exists or not
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
    for index, element in enumerate(readDataList): #check total location and cleaning up the location syntax before stuffing into array
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
        welcomeMessage = readDataList[index+1].strip()
        objects = readDataList[index+2].strip().split(',')
        connectingLocations = readDataList[index+3].strip().split(',')
        mobs = readDataList[index+4].strip().split(',')
        a = Location.Location(location, welcomeMessage, objects, connectingLocations, mobs)
        locations.append(a)
        index += 6
        i += 1

    return locations

def initializePerson(fileName = 'Person.txt'):
    wordsRemove = ["Name:","Health:","Attack:","Defense:","Inventory:","***"]
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
        fileInit.write("Name:\nHealth:\nAttack:\nDefense:\nInventory:\n***\n")
        fileInit.close()
    with open(fileName) as file:
        for line in file:
            readDataList.append(line.replace('\n', '').strip())
    for index, element in enumerate(readDataList):  # check total location and cleaning up the location syntax before stuffing into array
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
        a = Person.Person(name, health, attack, defense, inventory)
        persons.append(a)
        index += 6
        i += 1

    return persons

def initializeMobs(fileName = 'Mob.txt'):
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
    for index, element in enumerate(readDataList):  # check total mobs and cleaning up the location syntax before stuffing into array
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

def save(locationName = 'location.yaml', personName = 'person.yaml', mobName = 'mob.yaml'): #dumps all objects from the arrays into yaml files for save states
    with open(locationName, 'w+') as locationYaml:
        for element in locationArray:
            yaml.dump(element, locationYaml)
    with open(personName, 'w+') as personYaml:
        for element in personArray:
            yaml.dump(element, personYaml)
    with open(mobName, 'w+') as mobYaml:
        for element in mobArray:
            yaml.dump(element, mobYaml)

def load(locationName = 'location.yaml', personName = 'person.yaml', mobName = 'mob.yaml' ): #loads from yaml the objects into arrays
    global locationArray
    global personArray
    global mobArray
    with open(locationName) as locationYaml:
        locationArray = load(locationYaml)
    with open(personName) as personYaml:
        personArray =load(personYaml)
    with open(mobName) as mobYaml:
        mobArray = load(mobYaml)

def initializeGame():

    global locationArray
    global personArray
    global mobArray
    locationArray = initializeLocations()
    personArray = initializePerson()
    mobArray = initializeMobs()
