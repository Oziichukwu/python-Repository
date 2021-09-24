class Building:
    def __init__(self, name, discription, address,cohorts):
        self.name = name
        self.discription = discription
        self.address = address
        self.cohorts = cohorts
    def __str__(self) -> str:
        return self.name + "," + self.address
            
class Cohorts:
    def __init__(self,name,discription, natives):
        self.name = name
        self.discription = discription
        self.natives = natives

    def __str__(self) -> str:
        return self.name + "," + self.discription

class Natives:
    def __init__(self, scn, first_name, last_name, sex ):
        self.scn = scn
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self) -> str:
        return self.first_name + "," +  self.last_name              