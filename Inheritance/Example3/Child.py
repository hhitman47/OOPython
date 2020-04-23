from Inheritance.Example3.Parent import Parent

class Child(Parent):
    dog1 = Parent("Fread", "Dog west hunt")
    cat1 = Parent("Koko","wild cat")

    dog1.showInfo()
    cat1.showInfo()
