"""
Define a class person with constructor to initialize instance variable, also define a display method to print variables.
Inherit a class student from Person, make constructor to initialize variables and override display method of Person to display details of student.
"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # display method for Person class
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
    

class Student(Person):
    
    def __init__(self, name , age , section):
        Person.__init__(self,name, age)
        self.section = section
    
    # display method for Student class(overridding display method of class Person)
    def display(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)
    

P = Person("gaurav tiwari", 28)
P.display()
print("-------------------------------")

S = Student("Rajat Shukla", 24 , "Chemistry")
S.display()