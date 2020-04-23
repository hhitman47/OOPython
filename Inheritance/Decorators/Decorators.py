#Decorators
class Decorators:
    #plain, reguler , instance method
    def Function(self):
        return "This is a Normal Function : ", self

    @classmethod    #  cls = Decorators
    def classFunction(cls):
        return "This is a class Function : ", cls

    @staticmethod
    def staticFunction():
        return "This is a Static Funcation : "

myObject = Decorators()

print(myObject.Function())
print(myObject.classFunction())
print(myObject.staticFunction())

print(Decorators.classFunction())
print(Decorators.staticFunction())
#print(Decorators.Funcation())





