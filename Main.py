# This is the driving code for creating the different objects
# Special characters to indicate end of a section and end of a location
# End of location: ***

import LocationExtractor
import Mob
import Person


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
    i=0

    while i < locationTotal:
        location = readDataList[index].strip()
        welcomeMessage = readDataList[index+1].strip()
        objects = readDataList[index+2].strip().split(',')
        connectingLocations = readDataList[index+3].strip().split(',')
        mobs = readDataList[index+4].strip().split(',')
        a = LocationExtractor.Location(location, welcomeMessage, objects, connectingLocations, mobs)
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

    print(readDataList)
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


locationArray = initializeLocations()
personArray = initializePerson()

for element in locationArray:
    print(str(element))

for element in personArray:
    print(str(element))
