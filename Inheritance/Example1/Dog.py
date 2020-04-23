#Dog class
from Inheritance.Example1.Animal import Animal

class Dog(Animal):

  dog1 = Animal("Fread", "white" ,"Small", "west highland white terrier hunt")
  dog2 = Animal("jack" , "Back" ,"big", "Dobermann")

  dog1.Walk("slow")
  dog1.Sleep("After Noon")
  dog1.Eat("meat")


  dog1.AnimalCompleteInfo()


