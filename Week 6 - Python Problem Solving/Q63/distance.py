# DOWN, LEFT and RIGHT with a given step. The trace of robot movement is shown as the following: (Note : Take input from console)
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Please write a program to compute the distance from the current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.


from dis import Instruction
from math import sqrt
from random import choices


class distance:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def moveUp(self,steps):
        self.y2 += steps


    def moveDown(self,steps):
        self.y2 -= steps


    def moveLeft(self,steps):
        self.x2 -= steps


    def moveRight(self,steps):
        self.x2 += steps


    def calcDist(self):
        a = (self.x2 -self.x1)**2
        b = (self.y2 -self.y1)**2
        dist = round(sqrt(a + b))
        print(f'Distance from origin = {dist} units')

    def getCoordinates(self):
        print(f'\n origin (x1,y1) = {self.x1},{self.y1}  \n  (x2,y2) = {self.x2},{self.y2}')




step=[]
print(f'\n Enter steps \n Enter \'quit\' to Exit and calculate Dist')

while True:
    instruct = input()
    if instruct.lower() == 'quit':
        break

    step.append(instruct.split())

print(step)

rob = distance()

for i in step:
    if i[0].lower() == "up":
        rob.moveUp(int(i[1]))
    elif i[0].lower() == "down":
        rob.moveDown(int(i[1]))
    elif i[0].lower() == "left":
        rob.moveLeft(int(i[1]))
    elif i[0].lower() == "right":
        rob.moveRight(int(i[1]))
    
rob.getCoordinates()
rob.calcDist()