   
# Inherite
from Inheritance.Example2.Iot import Iot

class Student(Iot):

     def __init__(self, fname , lname , age , mobile , gender ,pro_lang):
       self.gender = gender
       self.pro_lang = pro_lang
       super(Student, self).__init__(fname , lname , age , mobile)

# Roll_1 = Student("Ishtiaq", "Hussain", 35, 304040404 )
# Roll_2 = Student("Ali","Khan", 25, 5599595)
# Roll_3 = Student("Jola","Irena", 33, 48393933)

#print(help(Iot))
#print(Roll_1.getStudentInfo())

Roll_1 = Student("Ishtiaq", "Hussain", 35, 304040404 ,'male','java')
Roll_2 = Student("Ali","Khan", 25, 5599595, "male", "C++")
Roll_3 = Student("Jola","Irena", 33, 48393933,"Female" ,"Python")

print(Roll_1.getStudentInfo(),"\nGender : ",Roll_1.gender, "\nLanguage :",Roll_1.pro_lang )
# print(help(Iot)) # important for get parent class Structure
#print(Roll_1.getStudentInfo())
