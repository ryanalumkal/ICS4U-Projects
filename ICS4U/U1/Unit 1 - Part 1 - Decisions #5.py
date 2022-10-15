# Name - Ryan Alumkal
# Grade - 12
# Description - Calculates number of discrimants and roots using values given from standard form
# Date -  September 20, 2022

#import 
import math

#user inputs for values a,b, and c of standard form
a = float(input("Enter the a value of the standard form of the quadratic equation: "))
b = float(input("Enter the b value of the standard form of the quadratic equation: " ))
c = float(input("Enter the c value of the standard form of the quadrati equation: "))


discrimanent = (b**2) - (4*a*c) #discriminant formula

#if statement using the results from the discrimanent
if discrimanent > 0: #if there are 2 solutions 
	solutions = 2
	print(f"\nThis equation has {solutions} solutions") #prints number of solutions 
	root1 = round(((-1*b) - math.sqrt((b**2)-(4*a*c)))/(2*a),2) #calculates the first root
	root2 = round(((-1*b) + math.sqrt((b**2)-(4*a*c)))/(2*a),2) #calculates the second root 
	print(f"\nThe solutions is {root1} and {root2}") #prints out the results of the roots 
elif discrimanent == 0: #if there is 1 soultion
	solutions = 1
	print(f"\nThis equation has {solutions} solutions") #prints out the number fo roots 
	root1 = round(((-1*b) - math.sqrt((b**2)-(4*a*c)))/(2*a),2) #calculates the only root
	print(f"\nThe solution is {root1}") #prints the root 
elif discrimanent < 0: #if there are no solutions 
	solutions = 0
	print(f"\nThis equation has {solutions} solutions") #prints out the number of roots


#END 