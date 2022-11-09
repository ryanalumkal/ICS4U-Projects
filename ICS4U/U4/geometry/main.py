# Name - Ryan Alumkal
# Grade - 12
# Description - 
# Date -  October 31, 2022

import geometry

def choice():
    while True:
        try:
            choice = int(input("Do you want to calculate for a rectangular prism(1) or cylinder(2): "))
            if choice == 1 or choice == 2:
                break
        except:
            print("Enter a proper value, [1] for rectangular prism or [2] for cylinder")
    return choice

def user_input(choice):
    length = int(input("Enter the length:")) 
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    if choice == 1:
        geometry.surface_area_rectangular_prism(length, width, height)
    if choice == 2: #if cylinder
        radius = int(input("Enter the radius: "))
        geometry.surface_area_cylinder(length,width,height,radius)
        #return radius
    #return length, width, height

def main():
    user_choice = choice()
    user_input(user_choice)
if __name__ == "__main__":
    main()