#import main
import math

def area_rectangle(length, width):
    rectangle_area = length * width
    return rectangle_area
def area_circle(radius):
    circle_area = math.pi*radius**2
    return circle_area 
def circumference(radius):
    circle_circumference = 2 * math.pi * radius
    return circle_circumference
def volume_rectangular_prism(length,width,height):
    rectangular_prism_volume = length * width * height
    return rectangular_prism_volume
def volume_cylinder(radius,height):
    cylinder_volume = math.pi * radius**2 * height
    return cylinder_volume
def surface_area_rectangular_prism(length, width, height):
    rectangle_area = area_rectangle(length, width)
    rectangular_prism_volume = volume_rectangular_prism(length, width, height)
    print(f"The area of the rectangle is {rectangle_area}")
    print(f"The volume of the rectangle is {rectangular_prism_volume}")
    surface_area = 2*(rectangle_area + (height * length) + (height * width))
    print(f"The surface area of the rectangle is {surface_area}")
    #call area_rectangle
def surface_area_cylinder(length, width, height,radius):
    circle_area = area_circle(radius)
    circle_circumference = circumference(radius)
    rectangle_area = area_rectangle(circle_circumference, width)
    #rectangular_prism_volume = volume_rectangular_prism(length, width, height)
    cylinder_volume = volume_cylinder(radius, height)
    print(f"The area of the circle is {circle_area}")
    print(f"The circumference of the circle is {circle_circumference}")
    print(f"The volume of the cylinder is {cylinder_volume}")
    surface_area = (2*circle_area) + (rectangle_area)
    print(f"The surface area of the circle is {surface_area}")
   
    #call area_circle, area_rectangle, and circumference