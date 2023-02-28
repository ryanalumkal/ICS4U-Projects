# Name - Ryan Alumkal
# Grade - 12
# Description - Asks user for desired input, the displays the results using Fraction class and static method
# Date - 2/27/2023

import math

#class
class Fraction:
    #creates numerator and denominator fields
    def __init__(self,numerator, denominator: int):
        self.num = numerator
        self.den = denominator

    def get_values(self: int) ->int: #returns values
        return self.num, self.den
    
    @staticmethod
    def product(f1, f2: object) ->object: #product method

        #unsimplified product
        ans_numerator= f1.num *f2.num #unsimplified numerator
        ans_denominator = f1.den *f2.den #unsimplified denominator

        gcd = math.gcd(ans_numerator, ans_denominator) #finds greated common denominator
        numerator = int(ans_numerator/gcd) #divides numerator by gcd, simplified numerator
        denominator = int(ans_denominator/gcd) #divides denominator by gcd, simplified denominator
        return (f"{str(numerator)}/{str(denominator)}") #returns value of fraction 
    
    @staticmethod
    def absolute(f1: object) ->object: #absolute method 
        abs_fraction = str(abs(f1.num))+"/"+ str(abs(f1.den))
        return abs_fraction #returns absolute value of numerator and denominator 
    
    @staticmethod
    def is_positive(f1: object) ->object: #is_positive method

        #conditions
        if f1.num == 0: #if numerator is 0, it is neither positive or negative 
            return "neither true or false"
        elif (f1.num/f1.den) > 0: #if the dividend is positive; fraction is positive
            return True
        else: #if the dividend is negative; fraction is negative
            return False
def user_input_choice_1(): #asks user for the numbers for different fractions
    while True:
        try:
            #user inputs 
            numerator1 = int(input("\nEnter the numerator of fraction 1: "))
            denominator1 = int(input("Enter the denominator of fraction 1: "))
            numerator2 = int(input("Enter the numerator of fraction 2: "))
            denominator2 = int(input("Enter the denominator of fraction 2: "))
            #if user input is valid
            if denominator1 !=0 and denominator2 !=0:
                return numerator1, denominator1, numerator2, denominator2
            else: #if user input is invalid
                print("Invalid input(s), enter a value greater than or equal to 0 for the numerators and a value greater than 0 for denominators")
        except: #if user input is invalid
            print("Enter a valid integer input")

def user_input_choice_2_and_3(): #asks user for the numbers for different fractions
    while True:
        try:
            #user input 
            numerator1 = int(input("\nEnter the numerator of fraction 1: "))
            denominator1 = int(input("Enter the denominator of fraction 1: "))
            #if user input is valid 
            if denominator1 !=0:
                return numerator1, denominator1
            else: #if invalid
                print("Invalid input(s), enter a value greater than or equal to 0 for the numerators and a value greater than 0 for denominators")
        except: #if user input is invalid
            print("Enter a valid integer input")

def user_choice(): #what user wants to perform
    while True: 
        print("\n1) Find the product \n2) Absolute value of faction \n3) Find if the fraction is positive or not \n4) Enter new value") #prints choices
        try: #while user input is invalid
            choice = int(input("\nEnter desired value (between 1 to 4): ")) #user input
            if choice == 1 or choice == 2 or choice == 3 or choice ==4: #if valid
                return choice
            else: #if invalid
                print("Enter a proper integer value")
        except: #if invalid 
            print("Enter a proper integer value")

#main function
def main():
    while True:
        choice = user_choice()
        if choice ==1: #if user wants to find product of two fractions 
            numerator1, denominator1, numerator2, denominator2 = user_input_choice_1()
            
            #assigns values
            f1 = Fraction(numerator1, denominator1)
            f2 = Fraction(numerator2, denominator2)

            #gets and prints result
            result = Fraction.product(f1,f2)
            print(f"The product of the two fractions is {result}")
      
        elif choice ==2: #if user wants to find absolute value of one fraction
            numerator1, denominator1 = user_input_choice_2_and_3()

            #assigns values
            f1 = Fraction(numerator1, denominator1)

            #gets and prints result
            result = Fraction.absolute(f1)
            print(f"The absolute value of {f1.num}/{f1.den} is {result}")
      
        elif choice ==3: #if user wants to find if a fraction is positive or negative
            numerator1, denominator1 = user_input_choice_2_and_3()
            #assigns values
            f1 = Fraction(numerator1, denominator1)
            
            #gets and prints result
            result = Fraction.is_positive(f1)
            print(f"It is {str(result).lower()} that fraction {f1.num}/{f1.den} is a positive fraction")
      
        elif choice ==4: #if user wants to end program
            print("Thank you for using the program")
            break

#main program 
if __name__ == "__main__":
    main()

