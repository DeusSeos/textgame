file = open('Location.txt', 'r')

class Location():
    def __init__(self, location, welcomeMessage, objects, connectingLocations):
        self.location = location # has to be a string
        self.welcomeMessage = welcomeMessage # has to be a string
        self.objects = objects # has to be a list
        self.connectingLocations = connectingLocations # has to be a list
