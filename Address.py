class Address:
    building_name=""
    town=""
    city=""
    zip=""
    state=""
    addresses = []

    def PrintAddresses():
        for addr in Address.addresses:
            print ("Your address is: " + addr.building_name + ", " + addr.town + ", " + addr.city + "-" + addr.zip + ", " + addr.state)
    
    def AddAddress():
        addr = Address()
        addr.building_name = input("Enter your building name: ")
        addr.town = input("Enter your town: ")
        addr.city = input("Enter your city: ")
        addr.zip = input("Enter your zip: ")
        addr.state = input("Enter your state: ")
        
        Address.addresses.append(addr);

        # print("Your building name is: " + building_name)
        # print("Your town is: " + town)
        # print("Your city is: " + city)
        # print("Your zip is: " + zip)
        # print("Your state is: " + state)

print("1. Add Address")
print("2. Print Addresses")

while input("Should Continue?: ").lower()=="true":
    stepNo=int(input("Enter Step No to execute:"))
    if stepNo == 1:
        print("Before calling AddAddress: ")
        Address.AddAddress()
        print("After calling AddAddress: ")
    elif stepNo == 2:
        Address.PrintAddresses()
