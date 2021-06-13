from Address import Address

addresses = []

def PrintAddresses(addresses):
    for addr in addresses:
        addr.PrintAddress()

def WriteAddressesToFile(addresses):
    addrFile = open("AddressFile.txt","a")
    for addr in addresses:
        addrFile.write(addr.ReturnAddressAsString())
        addrFile.write("\n")
    addrFile.close()

# w - write, r - read, r+ - read/write, a - append
def ReadAddressesFromFile():
    with open('AddressFile.txt') as f:
        for line in f.read().splitlines():
            print(line)

print("1. Add Address")
print("2. Print Addresses")

while input("Should Continue?: ").lower()=="true":
    stepNo=int(input("Enter Step No to execute:"))
    if stepNo == 1:
        building_name = input("Enter your building name: ")
        town = input("Enter your town: ")
        city = input("Enter your city: ")
        zip = input("Enter your zip: ")
        state = input("Enter your state: ")
        address = Address(building_name, town, city, zip, state)
        addresses.append(address)
    elif stepNo == 2:
        PrintAddresses(addresses)
    elif stepNo == 3:
        WriteAddressesToFile(addresses)
    elif stepNo == 4:
        ReadAddressesFromFile()