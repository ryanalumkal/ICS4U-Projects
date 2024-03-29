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
            if r != 0: #if radius is valid
                return x,y,r
            else: #if radius is invalid
                print("Enter a proper float value for radius (not equal to 0)")
        except: #if invalid
            print("Enter a proper float value")

def user_choice(): #what user wants to perform
    while True: 
        try: #while user input is invalid
            choice = int(input("\nEnter 1 to continue or 2 to end the program: ")) #user input
            if choice == 1 or choice == 2: #if valid
                return choice
            else: #if invalid
                print("Enter a proper integer value")
        except: #if invalid 
            print("Enter a proper integer value")

def main(): #main function
    while True:
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
    
        #assigns c3 to the smaller of the circles between c1 and c2, c1 if both have same area
        c3 = c1.smaller(c2) #finds the smaller circle
        print(f"The smaller circle c3 ({c3[0]}) has an area of {round(c3[1],2)}") #prints result
        choice = user_choice()
        if choice ==2:
            print("Thank you for using the program")
            break

#main program
if __name__ == "__main__": 
    main()
