# Name - Ryan Alumkal
# Grade - 12
# Description - Takes three float paraments, coordinates and radius, and converts radius to positive if negative
# Date - 2/20/2023

class Circle: #circle class
    def __init__(self,xcoordinate,ycoordinate, radius): #method 
        self.x = xcoordinate #x coordinate of circle
        self.y = ycoordinate#y coordinate of circle 
        if radius > 0: #if radius is positive
            self.r = radius #radius
        else: #if negative, make positive
            self.r = -radius

    def get_values(self): #returns values 
        return self.x, self.y, self.r

def user_input(): #gets user inputs: x and y coordinate and radius
    while True: #while user input is false
        try:
            x = float(input("Enter the x coordinate of the circle: "))
            y = float(input("Enter the y coordinate of the circle: "))
            r = float(input("Enter the radius of the circle: "))
            if r !=0: #if user input is not 0 (positive or negative)
                return x,y,r
            else: #if invalid
                print("Enter a proper float value")
        except: #if invalid
            print("Enter a proper float value")

def main(): #main function
    values = user_input() #gets user input
    c1 = Circle(values[0],values[1],values[2]) 
    values = c1.get_values() #gets new values
    print(values[0], values[1], values[2]) #prints values

#main program
if __name__ == "__main__":
    main()