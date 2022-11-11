#import main
import math

def area_rectangle(length, width):
    rectangle_area = round(length * width,2)
    return rectangle_area

def area_circle(radius):
    circle_area = round(math.pi*radius**2,2)
    return circle_area 

def circumference(radius):
    circle_circumference = round(2 * math.pi * radius,2)
    return circle_circumference

def volume_rectangular_prism(length,width,height):
    rectangular_prism_volume = round(length * width * height,2)
    return rectangular_prism_volume

def volume_cylinder(radius,height):
    cylinder_volume = round(math.pi * radius**2 * height,2)
    return cylinder_volume

def surface_area_rectangular_prism(length, width, height):
    rectangle_area = area_rectangle(length, width)
    rectangular_prism_volume = volume_rectangular_prism(length, width, height)
    print(f"The area of the rectangle is {rectangle_area}")
    print(f"The volume of the rectangle is {rectangular_prism_volume}")
    surface_area = round(2*(rectangle_area + (height * length) + (height * width)),2)
    print(f"The surface area of the rectangle is {surface_area}")
    #call area_rectangle

def surface_area_cylinder(height,radius):
    circle_area = area_circle(radius)
    circle_circumference = circumference(radius)
    rectangle_area = area_rectangle(circle_circumference, height)
    cylinder_volume = volume_cylinder(radius, height)
    print(f"The area of the circle is {circle_area}")
    print(f"The circumference of the circle is {circle_circumference}")
    print(f"The volume of the cylinder is {cylinder_volume}")
    surface_area = round((2*circle_area) + (rectangle_area),2)
    print(f"The surface area of the cylinder is {surface_area}")
   
    #call area_circle, area_rectangle, and circumference