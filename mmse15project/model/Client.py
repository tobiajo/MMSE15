from datetime import datetime





class Client:
    def __init__(self, id=0,email = '', name ='', address='',postalCode=0, city='', birthdate='1 jan 91'):
        self.id=id
        self.email = email
        self.name = name
        self.address = address
        self.postalCode = postalCode
        self.city = city
        self.birthdate =  datetime.strptime(birthdate, '%b-%d-%Y')


    def setAllData(self,values):
        self.id = values[0]
        self.email = values[1]
        self.name = values[2]
        self.address = values[3]
        self.postalCode = values[4]
        self.city = values[5]
        self.birthdate = datetime.strptime(values[6], '%b-%d-%Y')

    def getAllData(self,values): return (self.id,self.email,self.name,self.address,self.postalCode,self.city,self.birthdate)

    def getID(self): return self.id
    def getEmail(self): return self.email
    def getName(self): return self.name
    def getAddress(self): return self.address
    def getCity(self): return self.city
    def getBirthDate(self): return self.birthdate
    def getPostalCode(self): return self.postalCode

    def setID(self,id): self.id = id
    def setEmail(self,email): self.email = email
    def setName(self,name): self.name = name
    def setAddress(self,address): self.address = address
    def setPostalCode(self, pc): self.postalCode = pc
    def setCity(self): self.city
    def setBirthDate(self, bd): self.birthdate = datetime.strptime(bd, '%b-%d-%Y')