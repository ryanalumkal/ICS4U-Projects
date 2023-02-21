# Name - Ryan Alumkal
# Grade - 12
# Description - Two objects f1 and f2 with type Fraction are created and assigned values. The program performs the tasks: a) Double the value of f1.b) Invert f2.c) Make f1 equal to the (unsimplified) product of f1 and f2.d) Make f2 equal to the (unsimplified) sum of f1 and f2.and e) Make f1 equal to ∣f1∣ (the absolute value of f1).
# Date -  2/21/2023

class Fraction: #Fraction class
    num = 0 #numerator
    den = 0 #denominator 

def user_input(): #asks user for the numbers for different fractions
    while True:
        try:
            f1_fraction_numerator = int(input("For the fraction 'f1', enter the numerator: "))
            f1_fraction_denominator = int(input("For the fraction 'f1', enter the denominator: "))
            f2_fraction_numerator = int(input("For the fraction 'f2', enter the numerator: "))
            f2_fraction_denominator = int(input("For the fraction 'f2', enter the denominator: "))
            if f1_fraction_denominator !=0 and f2_fraction_denominator !=0:
                return f1_fraction_numerator,f1_fraction_denominator, f2_fraction_numerator, f2_fraction_denominator
            else:
                print("Invalid input(s), enter a value greater than or equal to 0 for the numerators and a value greater than 0 for denominators")
        except: #if user input is invalid
            print("Enter a valid integer input")
    

def user_choice(): #what user wants to perform
    while True: 
        print("\n1) Double the value of f1\n2) Invert f2 \n3) Make f1 equal to the (unsimplified) product of f1 and f2 \n4) Make f2 equal to the (unsimplified) sum of f1 and f2 \n5) Make f1 equal to ∣f1∣ (the absolute value of f1)\n6) Enter new values \n7) End program") #prints choices
        try: #while user input is invalid
            choice = int(input("\nEnter desired value (between 1 to 6): ")) #user input
            if choice == 1 or choice == 2 or choice == 3 or choice ==4 or choice == 5 or choice ==6 or choice ==7: #if valid
                return choice
            else: #if invalid
                print("Enter a proper integer value")
        except: #if invalid 
            print("Enter a proper integer value")
        
def double_f1(f1): #doubles value of f1
    f1.num*=2
    print(f"\n{f1.num}/{f1.den}") #prints result

def invert_f2(f2): #inverts value of f2
    numerator = f2.num
    f2.num = f2.den
    f2.den = numerator
    print(f"\n{f2.num}/{f2.den}") #prints result

def product_f1_f2(f1,f2): #makes f1 equal to the product of f1 and f2
    f1.num = f1.num * f2.num
    f1.den = f1.den * f2.den
    print(f"\n{f1.num}/{f1.den}") #prints result

def sum_f1_f2(f1,f2): #makes f2 equal to the sum of f1 and f2
    f2.num = (f1.num*f2.den) + (f2.num *f1.den)
    f2.den = (f1.den*f2.den)
    print(f"\n{f2.num}/{f2.den}") #prints result

def absolute_f1(f1): #makes f1 equal to absolute value of f1
    f1.num = abs(f1.num)
    f1.den = abs(f1.den)
    print(f"\n{f1.num}/{f1.den}") #prints result

def main(): #main function
    while True:
        values = user_input()
        while True: #while user wants to continue 
            f1_numerator = values[0]
            f1_denominator = values[1]
            f2_numerator = values[2]
            f2_denominator = values[3]
            f1 = Fraction() #defines f1
            f1.num = f1_numerator #defines numerator
            f1.den = f1_denominator #defines denominator 
            f2 = Fraction() #defines f2
            f2.num = f2_numerator #defines numerator
            f2.den = f2_denominator #defines denominator 

            choice = user_choice() #gets user choice 
            if choice == 1: #if user wants to double value of f1
                double_f1(f1)
            elif choice ==2: #if user wants to invert value of f2
                invert_f2(f2)
            elif choice ==3: # if user wants to make f1 equal to the product of f1 and f2
                product_f1_f2(f1,f2)
            elif choice ==4: #if user wants to make f2 equal to the sum of f1 and f2
                sum_f1_f2(f1,f2)
            elif choice ==5: #if user wants to make f1 equal to absolute value of f1
                absolute_f1(f1) 
            elif choice == 6 or choice ==7: #ends program
                break
        if choice == 7:
            print("\nThank you for using the program")
            break

#main program
if __name__ == "__main__":
    main()
