

class Location():
    def __init__(self, location, welcomeMessage, objects, connectingLocations):
        self.location = location
        self.welcomeMessage = welcomeMessage
        self.objects = objects
        self.connectingLocations = connectingLocations

    def getLocation(self):
        return self.location

    def getWelcomeMessage(self):
        return self.welcomeMessage

    def getObjects(self):
        return self.objects

    def getConnectingLocations(self):
        return self.connectingLocations

    def __str__(self):
        return "{}||{}||{}||{}".format(self.location, self.welcomeMessage, self.objects, self.connectingLocations)



