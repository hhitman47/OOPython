# Animal class
class Animal(object):

    def __init__(self , name , color, size , species ):
        self.name = name
        self.color = color
        self.size = size
        self.species = species

    def Eat(self , food):
        self.food = food

    def Sleep(self, sleepTiming):
        self.sleeptiming = sleepTiming

    def Walk(self, walkingStyle):
        self.walkingSyle = walkingStyle

    def AnimalCompleteInfo(self):
         print("Animal Name is : ", self.name , ",  Color is ", self.color , " Size and Species : " ,
               self.size , " ", self.species , " And Sleep During " , self.sleeptiming , " can ",
               self.walkingSyle , " and eat only ", self.food)
