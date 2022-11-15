# Name - Ryan Alumkal
# Grade - 12
# Description - Calculates various values given whether the user wants to calculate values for a rectangular prism or cylinder
# Date -  November 15, 2022

import geometry #imports calculations from geometry.py

def user_shape(): #user's desired shape
    while True:
        try:
            choice = int(input("Do you want to calculate for a rectangular prism(1) or cylinder(2): ")) #user input
            if choice == 1 or choice == 2: #if choice is valid
                break
            else: #if user input is invalid 
                print("Enter a proper value, [1] for rectangular prism or [2] for cylinder")
        except: #if user input is invalid 
            print("Enter a proper value, [1] for rectangular prism or [2] for cylinder")
    return choice

def user_input(choice): #asks user for measurements 
    if choice == 1: #if rectangle 
        while True:
            try:
                width = float(input("Enter the width: "))
                length = float(input("Enter the length: "))
                height = float(input("Enter the height: ")) 
                if width > 0 and length > 0 and height >0: #if valid
                    break
                else: #if invalid 
                    print("Print a correct float value")  
            except: #if invalid 
                print("Print a correct float value")  
        values = [width, length, height] #measurements for a rectangular prism
    else: #if cylinder
        while True:
            try:
                radius = float(input("Enter the radius: "))
                height = float(input("Enter the height: ")) 
                if radius > 0 and height >0: #if valid 
                    break
                else: #if invalid 
                    print("Print a correct float value")
            except: #if invalid 
                print("Print a correct float value")
        values = [radius, height] #measurements for a cylinder 
    return values #returns measurements 

def results(choice, values): #prints results of the measurements for various values 
    if choice == 1: #if rectangular prism
        rectangle_area1 = round(geometry.area_rectangle(values[1], values[0]),2) #area of rectangle; values = length and width
        rectangle_area2 = round(geometry.area_rectangle(values[1],values[2]),2)  #area of rectangle; values = length and height
        rectangle_area3 = round(geometry.area_rectangle(values[0],values[2]),2) #area of rectangle; values = width and height
        rectangular_prism_volume = round(geometry.volume_rectangular_prism(values[1], values[0], values[2]),2) #rectangular prism volume; values = length, width, height
        rectangular_prism_surface_area = round(geometry.surface_area_rectangular_prism(values[1], values[0], values[2]),2) # rectangular prism surface area; values = length, width, and height
        print(f"The area of the rectangle with measurements {values[1]} and {values[0]} is {rectangle_area1}") #prints area of rectangle with measurements of length and width
        print(f"The area of the rectangle with measurements {values[1]} and {values[2]} is {rectangle_area2}") #prints area of rectangle with measurements of length and height
        print(f"The area of the rectangle with measurements {values[0]} and {values[2]} is {rectangle_area3}") #prints area of rectangle with measurements of width and height
        print(f"The volume of the rectangular prism is {rectangular_prism_volume}") #prints volume of rectangular prism
        print(f"The surface area of the rectangle is {rectangular_prism_surface_area}") #prints surface area of rectangular prism
    else: #if cylinder 
        circle_area = round(geometry.area_circle(values[0]),2) #area of circle; value = radius
        circle_circumference = round(geometry.circumference(values[0]),2) #circumference of circle; value = radius 
        cylinder_volume = round(geometry.volume_cylinder(values[0], values[1]),2) #volume of cylinder; values = radius and height
        cylinder_surface_area  = round(geometry.surface_area_cylinder(values[1], values[0]),2) #surface area of cylinder; values = height and radius
        print(f"The area of the circle is {circle_area}") #prints area of circle 
        print(f"The circumference of the circle is {circle_circumference}") #prints circumference of circle 
        print(f"The volume of the cylinder is {cylinder_volume}") #prints volume of cylinder 
        print(f"The surface area of the cylinder is {cylinder_surface_area }") #prints surface area of cylinder
   
def user_continue(): #if user wants to continue or not 
    while True: #loop
        try:
            option = str(input("Do you want to continue [Y/N]: "))   #user choice 
            if option == "Y" or option == "y" or option == "N" or option == "n": #if choice is valid 
                break
            else:
                print("Enter a valid option [Y or N]") #if input is not valid 
        except:
            print("Enter a valid option [Y or N]") #if user input is not valid 
    return option    

def main(): #main function
    while True: #while user wants to continue 
        user_choice = user_shape() #user's desired shape
        values = user_input(user_choice) #measurements 
        results(user_choice, values) #values/results 
        choice = user_continue() #if user wants to continue or not
        if choice == "N" or choice == "n": #if user does not want to continue
            print("Thank you for using the program") 
            break #ends program

#main program

if __name__ == "__main__": 
    main()