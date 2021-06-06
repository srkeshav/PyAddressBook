class Address:
    def config(self):
        print("{}, {}, {}-{}, {}".format(self.FlatNo,self.BuildingName,self.City,self.Zip, self.State))
    FlatNo=501
    BuildingName="Suryalok Tower"
    Zip=401101 
    City="Mumbai"
    State="Maharashtra"
#501, Suryalok Tower, Mumbai-401101, Maharashtra
com = Address()
Address.config(com)