"""
Write a class Circle with a constructor to initialize variables like co-ordinates of center of a circle(x,y) and radius.
define methods to calculate perimeter, area, and a method to check if a given point belongs to circle.
"""

from math import pi,sqrt

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter (self):
        return  2 * pi * self.r


    def area (self):
        return  pi * self.r**2
    

   
    def calDist (self, x, y):
        dist=sqrt(((x-self.a)**2 + (y-self.b)**2))
        print(f"distance of given point({x},{y}) from center of circle is {dist} units ")
        
        if dist<=self.r:
            return True
        else:
            return False

    
    # method to test if given point blong to the circle or not 
    def test_belong (self, x, y):
        if (self.calDist (x, y) ):
            print (f"Therefore the point: ({x},{y}) belongs to the circle C")
        else:
            print (f"Therefore the point: ({x},{y}) does not belong to the circle C")



C = Circle (3,7,3)

print ("the perimeter of the circle C is:", C.perimeter() )
print ("the area of circle C is:", C.area())

print(f"\nco-ordinates of center of circle is({C.a},{C.b}) with radius = {C.r}")

# testing if point belong to the circle or not
C.test_belong(3,2) 


