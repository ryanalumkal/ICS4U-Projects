# Name - Ryan Alumkal
# Grade - 12
# Description - Asks user for desired input, the displays the results using Fraction class and static method
# Date - 2/27/2023


import math

#class
class Fraction:

    @staticmethod
    def product(fraction1, fraction2: object) ->object: #product method

        #assigns values
        f1numerator = int(fraction1.split('/')[0])
        f1denominator = int(fraction1.split('/')[1])
        f2numerator = int(fraction2.split('/')[0])
        f2denominator = int(fraction2.split('/')[1])
        ans_numerator= f1numerator *f2numerator #unsimplified numerator
        ans_denominator = f1denominator *f2denominator #unsimplified denominator

        gcd = math.gcd(ans_numerator, ans_denominator) #finds greated common denominator
        numerator = int(ans_numerator/gcd) #divides numerator by gcd, simplified numerator
        denominator = int(ans_denominator/gcd) #divides denominator by gcd, simplified denominator
        return (f"{str(numerator)}/{str(denominator)}") #returns value of fraction 
    
    @staticmethod
    def absolute(fraction1: object) ->object: #absolute method 
        f1numerator = int(fraction1.split('/')[0])
        f1denominator = int(fraction1.split('/')[1])
        abs_fraction = str(abs(f1numerator))+"/"+ str(abs(f1denominator))
        return abs_fraction #returns absolute value of numerator and denominator 
    
    @staticmethod
    def is_positive(fraction1: object) ->object: #is_positive method
        f1numerator = int(fraction1.split('/')[0])
        f1denominator = int(fraction1.split('/')[1])
        if f1numerator == 0: #if numerator is 0, it is neither positive or negative 
            return "neither true or false"
        elif f1numerator > 0 and f1denominator > 0: #if numerator AND denominator is positive, return true 
            return True
        elif f1numerator <0 and f1denominator <0: #both are negative, cancels out
            return True
        else: #if fraction is negative, return false 
            return False

def user_input_choice_1(): #asks user for the numbers for 2 different fractions 
    while True:
        try:
            fraction1 = input("Enter a fraction in format 'n/d': ")
            fraction2 = input("Enter another fraction in format 'n/d': ")
            if fraction1.split('/')[1] !=0 and fraction2.split('/')[1]: #if inputs are valid, denominators are not 0
                return fraction1, fraction2
            else: #if not...
                print("Invalid input(s), enter a value greater than or equal to 0 for the numerators and a value greater than 0 for denominators")
        except: #if user input is invalid
            print("Enter a valid integer input")

def user_input_choice_2_and_3(): #asks user for the numbers for 1 fraction
    while True:
        try:
           fraction1 = input("Enter a fraction in format 'n/d': ")
           if fraction1.split('/')[1] !=0: #if inputs are valid, denominator is not 0
                return fraction1
           else:
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
            fraction1, fraction2 = user_input_choice_1()
            result = Fraction.product(fraction1, fraction2)
            print(f"The product of the two fractions is {result}")
      
        elif choice ==2: #if user wants to find absolute value of one fraction
            fraction1 = user_input_choice_2_and_3()
            result = Fraction.absolute(fraction1)
            print(f"The absolute value of {fraction1} is {result}")
      
        elif choice ==3: #if user wants to find if a fraction is positive or negative
            fraction1 = user_input_choice_2_and_3()
            result = Fraction.is_positive(fraction1)
            print(f"It is {str(result).lower()} that fraction {fraction1} is a positive fraction")
      
        elif choice ==4:
            print("Thank you for using the program")
            break

#main program 
if __name__ == "__main__":
    main()

