# Write a program to print the sum of the polygon angle side in degree . Take side of angle input from console 

def angleSum():
    try:

        while True:
            sides = abs(int(input("Enter no. of sides of Polygon : ")))
            if sides < 3:
                print(f'Sides cannot be less than 3 ')
            else:
                sum = (sides-2)*180
                print(f'Sum of angles of polygon with {sides} sides = {sum} degree')
                break


    except ValueError:
        print("Invalid Value type")



angleSum()

