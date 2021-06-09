class Address:
    building_name=""
    street_town=""
    city=""
    zip=""
    state=""

    def AddAddress():
        com = Address()
        building_name = input("Enter your building name: ")
        street_town = input("Enter your street and town: ")
        city = input("Enter your city: ")
        zip = input("Enter your zip: ")
        state = input("Enter your state: ")
        
        print ("Your address is: " + building_name + ", " + street_town + ", " + city + "-" + zip + ", " + state)
        
        # print("Your building name is: " + building_name)
        # print("Your street and town is: " + street_town)
        # print("Your city is: " + city)
        # print("Your zip is: " + zip)
        # print("Your state is: " + state)

Address.AddAddress()