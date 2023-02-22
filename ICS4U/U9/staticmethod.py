class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    @staticmethod
    def product():
        
def user_input(): #asks user for the numbers for different fractions
    while True:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            
            if denominator !=0:
                return numerator, denominator
            else:
                print("Invalid input(s), enter a value greater than or equal to 0 for the numerators and a value greater than 0 for denominators")
        except: #if user input is invalid
            print("Enter a valid integer input")

def main():
    numerator, denomiator = user_input()
    fraction = Fraction(numerator, denomiator)
    print(numerator, denomiator)

if __name__ == "__main__":
    main()

