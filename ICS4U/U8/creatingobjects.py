# Name - Ryan Alumkal
# Grade - 12
# Description - Two objects f1 and f2 with type Fraction are created and assigned values. The program performs the tasks: a) Double the value of f1.b) Invert f2.c) Make f1 equal to the (unsimplified) product of f1 and f2.d) Make f2 equal to the (unsimplified) sum of f1 and f2.and e) Make f1 equal to ∣f1∣ (the absolute value of f1).
# Date -  2/20/2023

class Fraction: #Fraction class
    num = 0 #numerator
    den = 0 #denominator 
def user_choice(): #what user wants to perform
    while True: 
        print("\n1) Double the value of f1\n2) Invert f2 \n3) Make f1 equal to the (unsimplified) product of f1 and f2 \n4) Make f2 equal to the (unsimplified) sum of f1 and f2 \n5) Make f1 equal to ∣f1∣ (the absolute value of f1)\n6) End program") #prints choices
        try: #while user input is invalid
            choice = int(input("\nEnter desired value (between 1 to 6): ")) #user input
            if choice == 1 or choice == 2 or choice == 3 or choice ==4 or choice == 5 or choice ==6: #if valid
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
    while True: #while user wants to continue 
        f1 = Fraction() #defines f1
        f1.num = 3 #defines numerator
        f1.den = 4 #defines denominator 
        f2 = Fraction() #defines f2
        f2.num = 5 #defines numerator
        f2.den = 6 #defines denominator 

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
        elif choice == 6: #ends program
            print("\nThank you for using the program")
            break

#main program
if __name__ == "__main__":
    main()