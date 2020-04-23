
class Parent(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def showInfo(self):
        print("Pet Name is > ",self.name, " and it is a " , self.species)
