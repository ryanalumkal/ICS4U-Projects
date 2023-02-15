# Name - Ryan Alumkal
# Grade - 12
# Description - 
# Date - 

import math

class Circle:
    x = 0.0 #x coordinate of circle
    y = 0.0 #y coordinate of circle 
    r = 0.0 #radius

    def area_circle(self):
        return (math.pi*self.r**2)
    def smaller(self,c2):
        c1_area = (math.pi*self.r**2)
        c2_area = (math.pi*c2.r**2)
        if c1_area >= c2_area:
            return c1_area
        else:
            return c2_area

def user_input():
    while True:
        try:
            x = float(input("Enter the x coordinate of the circle: "))
            y = float(input("Enter the y coordinate of the circle: "))
            r = float(input("Enter the radius of the circle: "))
            if r > 0:
                return x,y,r
        except:
            print("Enter a proper float value")
def main():
    values1 = user_input()
    c1 = Circle()
    c1.x = values1[0]
    c1.y = values1[1]
    c1.r = values1[2]
    area_of_circle1 = c1.area_circle()
    print(f"The area of the circle 1 is {round(area_of_circle1,2)}")
    values2 = user_input()
    c2 = Circle()
    c2.x = values2[0]
    c2.y = values2[1]
    c2.r = values2[2]
    area_of_circle2 = c2.area_circle()
    print(f"The area of the circle 2 is {round(area_of_circle2,2)}")
    c3 = c1.smaller(c2)
    print(c3)

if __name__ == "__main__":
    main()