# This is the driving code for creating the different objects
# Special characters to indicate end of a section and end of a location
# End of section: ||
# End of location: ***

readDataList = []

try: #checks to see if file exists or not
    with open('Location.txt') as fileInit:
        if (fileInit.read() == ''):
            print('File exists but is empty. Will append structure to file')
        else:
            print("File exists. Structure hasn't been checked.")
except:
    print("File doesn't exist ")
    fileInit = open('Location.txt', 'w+')
    fileInit.write("Location:\nWelcome Message:\nObjects:\nConnecting Locations:\nMobs:\n***")

with open('Location.txt') as file:
    for line in file:
        readDataList.append(line)


