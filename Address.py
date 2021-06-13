class Address:
    
    def __init__(self, building_name, town, city, zip, state):
        self.building_name = building_name
        self.town = town
        self.city = city
        self.zip = zip
        self.state = state

    def PrintAddress(self):
        print ("Your address is: " + self.building_name + ", " + self.town + ", " + self.city + "-" + self.zip + ", " + self.state)

    def ReturnAddressAsString(self):
        return "Your address is: " + self.building_name + ", " + self.town + ", " + self.city + "-" + self.zip + ", " + self.state