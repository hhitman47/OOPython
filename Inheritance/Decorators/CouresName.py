#Decorators
class CourseName:
    def __init__(self,name):
        self.name = name
        print("New course object is created : ", name)

    @property
    def nameCourse(self):
        return self.name

    @nameCourse.setter
    def nameCourse(self, name):
        print(self.name , "- Course name Updated too ...! :",name)
        self.name = name

#create  courses object
iotObj = CourseName('IOT')
madObj = CourseName('Mobile App Development')
robObj = CourseName('Robotic')


#Diplay courses name
print("All courses object created so far....! ")
print(iotObj.nameCourse)
print(madObj.nameCourse)
print(robObj.nameCourse)


#update or edit course name
iotObj.nameCourse = 'IoT2020'
#show edit course name
print("Updated Course name Display : ",iotObj.nameCourse)
