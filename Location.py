

class Location():
    def __init__(self, locationName = '', welcomeMessage = '', objects = [], connectingLocations = [], mobs = []):
        self.locationName = locationName
        self.welcomeMessage = welcomeMessage
        self.objects = objects
        self.connectingLocations = connectingLocations
        self.mobs = mobs

    def getLocation(self):
        return self.locationName

    def getWelcomeMessage(self):
        return self.welcomeMessage

    def getObjects(self):
        return self.objects

    def getConnectingLocations(self):
        return self.connectingLocations

    def getMobs(self):
        return self.mobs


    def __str__(self):
        return "{}||{}||{}||{}||{}".format(self.locationName, self.welcomeMessage, self.objects, self.connectingLocations,self.mobs)



