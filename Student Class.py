from datetime import date


class Person:
    def __init__(self,n,e,birthday):
        self.__name = n
        self.__email = self.CheckEmail(e) #CheckEmail is defined in Method --> we use self.
        self.__age = self.calculateAge(birthday) #Same remark

    def CheckEmail(self,email):
        return "@" in email and "." in email and "@." not in email

    def calculateAge(self,birthday):
        today = date.today()
        self.__age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        return self.__age
    def getAge(self):
        return self.__age
    def setName(self,newName):
        self.__name = newName
    def getName(self):
        return self.__name
    def setEmail(self,newEmail):
        if self.CheckEmail(newEmail):
            self.__email = newEmail
    def getEmail(self):
        return self.__email
    #Print, returns all class's attributes
    def __str__(self):
        return "Name: {}, Email: {}, Age: {}".format(self.__name, self.__email, self.__age)
    #Check if two Person instances have the same name
    def __eq__(self, other):
        return (self.__name == other.__name)

class Student(Person):
    __courses = {"CS":0,"French":0,"Stat":0}
    __AverageGrade = 0
    def __init__(self,n,e,birthday,SID):
        Person.__init__(self,n,e,birthday)
        self.__SID = SID
    def AddCourse(self,CourseID,result):
        Student.__courses[CourseID] = result
    def calculateAverage(self):
        for i in Student.__courses:
            Student.__AverageGrade += Student.__courses[i]
        return Student.__AverageGrade / len(Student.__courses)
    def get_SID(self):
        return self.__SID
    def get_courses(self):
        return Student.__courses
    def get_AverageGrade(self):
        return self.calculateAverage()
    def set_SID(self,SID):
        self.__SID = SID
    def __str__(self):
        print(Person.__str__(self))
        return "SID = {}".format(self.__SID)
    def __lt__(self, other):
        return self.get_AverageGrade() < other.get_AverageGrade()

Student1 = Student("Student1","studnet1@gmail.com", date(2001,3,22), 10014555)
Student1.AddCourse("CS",80)
Student1.AddCourse("French",60)
Student1.AddCourse("Stat",90)

Student2 = Student("Student2","studnet2@gmail.com",date(2001,8,10),10514355)
Student2.AddCourse("CS",100)
Student2.AddCourse("French",100)
Student2.AddCourse("Stat",100)

Student3 = Student("Student3","studnet3@gmail.com", date(2001,10,10), 10500550)
Student2.AddCourse("CS",40)
Student2.AddCourse("French",100)
Student2.AddCourse("Stat",30)

print(Student1)

List = [Student3, Student2, Student1]

List.sort()
for x in List:
    print(x.getName())



