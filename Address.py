class Address:
    def Address(self):
        County = self.State
        print("{}, {}, \n{}-{}, \n{}".format(self.FlatNo,self.BuildingName,self.City,self.Zip,County))
    FlatNo=501
    BuildingName="Jonas Tower"
    Zip=302101 
    City="Hyderabad"
    State="Kolkata"
#501, Jonas Tower, Hyderabad-302101, Kolkata
com = Address()
#Address.print(com)
print('Building Name: ' + com.BuildingName + ' City: ' + com.City + ' State: ' + com.State + '-' + str(com.Zip))