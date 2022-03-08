""" 
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.
"""

class Rectangle:
    # define constructor with attributes: length and width 
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    # Create Perimeter method
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    # Create area method
    def Area(self):
        return self.length*self.width   
    
    # create display method
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.Perimeter())
        print("The area of rectangle is: ", self.Area())



class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height
        
    # define Volume method
    def volume(self):
        return self.length*self.width*self.height
        
rect= Rectangle(7 , 5)

# we can also change values of instance object by following statements
# rect.length=10 
# rect.width=8

rect.display()

print("----------------------------------")

parpipe= Parallelepipede(7 , 5 , 2)
print("the volume of parpipe is: " , parpipe.volume())

