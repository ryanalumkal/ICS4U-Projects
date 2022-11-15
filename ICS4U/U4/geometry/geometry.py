#IMPORTS 
import math 

def area_rectangle(length, width): #calculates area of rectangle 
    rectangle_area = length * width
    return rectangle_area

def area_circle(radius): #calculates area of circle
    circle_area = math.pi*radius**2
    return circle_area 

def circumference(radius): #calculates circumference of circle 
    circle_circumference = 2 * math.pi * radius
    return circle_circumference

def volume_rectangular_prism(length,width,height): #calculates volume of rectangular prism
    rectangular_prism_volume = length * width * height
    return rectangular_prism_volume

def volume_cylinder(radius,height): #calculates volume of cylinder 
    cylinder_volume = math.pi * radius**2 * height
    return cylinder_volume

def surface_area_rectangular_prism(length, width, height): #calculates surface area of rectangle 
    rectangle_area1 = area_rectangle(length, width) #area of rectangle 
    rectangle_area2 = area_rectangle(length,height) #area of rectangle 
    rectangle_area3 = area_rectangle(width,height) #area of rectangle 
    rectangular_prism_surface_area = (2*rectangle_area1 + 2*rectangle_area2 + 2*rectangle_area3) #calculates surface area from area(s) of rectangle
    return  rectangular_prism_surface_area

def surface_area_cylinder(height,radius): #calculates surface area of cylinder 
    circle_area = area_circle(radius) #area of circle 
    circle_circumference = circumference(radius) #circumference of circle
    rectangle_area = area_rectangle(circle_circumference, height) #area of the "rectangular circle" part of the cylinder
    cylinder_surface_area = ((2*circle_area) + (rectangle_area)) #calculates surface area from previous measurements 
    return cylinder_surface_area  
  