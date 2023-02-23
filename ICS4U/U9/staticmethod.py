class Fraction:

    @staticmethod
    def product(f1numerator, f1denominator, f2numerator, f2denominator): #product method
        ans_numerator= f1numerator *f2numerator #unsimplified numerator
        ans_denominator = f1denominator *f2denominator #unsimplified denominator

        n_placeholder = ans_numerator #placeholder numerator for gcd calculations 
        d_placeholder = ans_denominator #placeholder denominator for gcd calculations

        #to find lowest term factor
        while True: #loops till greatest common factor is found
            if d_placeholder == 0: #if denominator is 0, numerator is gcd
                gcd = n_placeholder #greatest common denominator
                break
            else:  #if not... 
                n_placeholder = d_placeholder #replaces numerator with previous denominator 
                d_placeholder = n_placeholder%d_placeholder #new denominator is remainder of numerator and denominator
                
        numerator = int(ans_numerator/gcd) #divides numerator by gcd, simplified umerator
        denominator = int(ans_denominator/gcd) #divides denominator by gcd, simplified denominator
        return numerator, denominator #returns values of fraction 
    
    @staticmethod
    def asbsolute(f1numerator, f1denominator): #absolute method 
        return abs(f1numerator), abs(f1denominator) #returns absolute value of numerator and denominator 
    
    @staticmethod
    def is_positive(f1numerator, f1denominator): #is_positive method
        if f1numerator == 0: #if numerator is 0, it is neither positive or negative 
            return "1neither true or false"
        elif f1numerator > 0 and f1denominator > 0: #if numerator AND denomiator is positive, return true 
            return True
        else: #if fraction is negative, return false 
            return False

def user_input_choice_1(): #asks user for the numbers for 2 different fractions 
    while True:
        try:
            numerator1 = int(input("\nEnter the numerator of fraction 1: "))
            denominator1 = int(input("Enter the denominator of fraction 1: "))
            numerator2 = int(input("Enter the numerator of fraction 2: "))
            denominator2 = int(input("Enter the denominator of fraction 2: "))
            if denominator1 !=0 and denominator2 !=0:
                return numerator1, denominator1, numerator2, denominator2
            else:
                print("Invalid input(s), enter a value greater than or equal to 0 for the numerators and a value greater than 0 for denominators")
        except: #if user input is invalid
            print("Enter a valid integer input")

def user_input_choice_2_and_3(): #asks user for the numbers for 1 fraction
    while True:
        try:
            numerator1 = int(input("\nEnter the numerator of fraction 1: "))
            denominator1 = int(input("Enter the denominator of fraction 1: "))
            if denominator1 !=0:
                return numerator1, denominator1
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
        if choice ==1:
            f1numerator, f1denominator, f2numerator, f2denominator = user_input_choice_1()
            result_numerator, result_denominator = Fraction.product(f1numerator, f1denominator, f2numerator, f2denominator)
            print(f"The product of the two fractions is {result_numerator}/{result_denominator}")
      
        elif choice ==2:
            f1numerator, f1denominator = user_input_choice_2_and_3()
            result_numerator, result_denominator = Fraction.asbsolute(f1numerator, f1denominator)
            print(f"The absolute value of {f1numerator}/{f1denominator} is {result_numerator}/{result_denominator}")
      
        elif choice ==3:
            f1numerator, f1denominator = user_input_choice_2_and_3()
            result_true_or_false = Fraction.is_positive(f1numerator, f1denominator)
            print(f"It is {str(result_true_or_false).lower()} that fraction {f1numerator}/{f1denominator} is a positive fraction")
      
        elif choice ==4:
            print("Thank you for using the program")
            break

#main program 
if __name__ == "__main__":
    main()

