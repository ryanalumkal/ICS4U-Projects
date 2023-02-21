# Name - Ryan Alumkal
# Grade - 12
# Description - Returns area of 2 circles, finds the smaller circle
# Date - 2/21/2023

import math

class Circle: #Circle class
    x = 0.0 #x coordinate of circle
    y = 0.0 #y coordinate of circle 
    r = 0.0 #radius

    def area_circle(self): #calculates area of a circle
        return (math.pi*self.r**2)
    def smaller(self,c2): #finds which circle is smaller
        c1_area = (math.pi*self.r**2)
        c2_area = (math.pi*c2.r**2)
        if c1_area > c2_area: 
            return "Circle 2", c2_area #if c2 is smaller, return this
        else:
            return "Circle 1 ", c1_area #if c2 is larger or equal to c1, return c1

def user_input(): #gets circle measurements 
    while True: #while invalid
        try:
            #gets x and y value of center of circle and its radius
            x = float(input("Enter the x coordinate of the circle: "))
            y = float(input("Enter the y coordinate of the circle: "))
            r = float(input("Enter the radius of the circle: "))
            if r != 0: #if valid
                return x,y,r
        except: #if invalid
            print("Enter a proper float value")
def main(): #main function
    values1 = user_input() #gets values of circle 1
    #assigns values of circle 1
    c1 = Circle()
    c1.x = values1[0]
    c1.y = values1[1]
    c1.r = values1[2]
    area_of_circle1 = c1.area_circle() #gets area of circle 1
    print(f"The area of the circle 1 is {round(area_of_circle1,2)}")

    values2 = user_input() #gets values of circle 2
    #assigns values of circle 2
    c2 = Circle()
    c2.x = values2[0]
    c2.y = values2[1]
    c2.r = values2[2]
    area_of_circle2 = c2.area_circle() #gets area of circle 2
    print(f"The area of the circle 2 is {round(area_of_circle2,2)}")
    c3 = c1.smaller(c2) #finds the smaller circle
    print(f"{c3[0]} has a radius of {round(c3[1],2)}") #prints result

#main program
if __name__ == "__main__": 
    main()
