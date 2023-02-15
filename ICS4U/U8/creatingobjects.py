# Name - Ryan Alumkal
# Grade - 12
# Description - 
# Date -  

class Fraction:
    num = 0 #numerator
    den = 0 #denominator 

def user_choice():
    while True:
        print("\n1) Double the value of f1\n2) Invert f2 \n3) Make f1 equal to the (unsimplified) product of f1 and f2 \n4) Make f2 equal to the (unsimplified) sum of f1 and f2 \n5) Make f1 equal to ∣f1∣ (the absolute value of f1)\n6) End program")
        try:
            choice = int(input("\nEnter desired value (between 1 to 6): "))
            if choice == 1 or choice == 2 or choice == 3 or choice ==4 or choice == 5 or choice ==6:
                return choice
            else:
                print("Enter a proper integer value")
        except:
            print("Enter a proper integer value")
        
def double_f1(f1):
    f1.num*=2
    print(f"\n{f1.num}/{f1.den}")
def invert_f2(f2):
    numerator = f2.num
    f2.num = f2.den
    f2.den = numerator
    print(f"\n{f2.num}/{f2.den}")
def product_f1_f2(f1,f2):
    f1.num = f1.num * f2.num
    f1.den = f1.den * f2.den
    print(f"\n{f1.num}/{f1.den}")
def sum_f1_f2(f1,f2):
    f2.num = (f1.num*f2.den) + (f2.num *f1.den)
    f2.den = (f1.den*f2.den)
    print(f"\n{f2.num}/{f2.den}")
def absolute_f1(f1):
    f1.num = abs(f1.num)
    f1.den = abs(f1.den)
    print(f"\n{f1.num}/{f1.den}")

def main():
    while True:
        f1 = Fraction()
        f1.num = 3
        f1.den = 4
        f2 = Fraction()
        f2.num = 5
        f2.den = 6

        choice = user_choice()
        if choice == 1:
            double_f1(f1)
        elif choice ==2:
            invert_f2(f2)
        elif choice ==3:
            product_f1_f2(f1,f2)
        elif choice ==4:
            sum_f1_f2(f1,f2)
        elif choice ==5:
            absolute_f1(f1)
        elif choice == 6:
            print("\nThank you for using the program")
            break

if __name__ == "__main__":
    main()