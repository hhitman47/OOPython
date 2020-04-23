
class Iot(object):


    # student_name = ""
    # student_age = ""
    # student_mobile = ""

    # Constructor

   # Constructor take 4 perimeters
    def __init__(self, fname , lname , age , mobile ):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.mobile = mobile
        self.email = fname + '.' + lname + '@iot.edu.pk'

     # To set or add  Student contact numner
    # def setStudentMobile(self,mobile):
    #     self.mobile = mobile

    # To get Student Info
    def getStudentInfo(self):
        # Will return information of Student Objecct
        return '{} {} {} {} {} {} {}' .format("Name : "+ self.fname + " "+self.lname ,"\nAge : " , self.age , "\nMobile : " , self.mobile , "\nEmail :",self.email)


