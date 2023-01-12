# Name - Ryan Alumkal
# Grade - 12
# Description - Returns a user-inputted fraction in lowest terms 
# Date -  1/12/2023


def user_input(): #Asks user for an input    
    while True:
        try: #check if user input is valid
            count_divide = 0 #counts the number of "/"
            count_num = 0 #counts the number of invalid characters
            fraction = input("Enter a positive fraction in the format 'n/d': ") #user input
            if fraction.count("/") == 1:
                fraction = fraction.split("/")
                numerator = int(fraction[0])
                denominator = int(fraction [1])
                if numerator > 0 and denominator > 0:
                    return numerator, denominator
                else:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")
        except:
            print("Enter a valid input")

def greatest_common_divisor(n, d): #finds the gcd of the numerator and denominator; Euclid's algorithm
    if (d == 0): #if denominator is 0, numerator is gcd
        return n #returns numerator
    else: #if not... 
        return greatest_common_divisor(d, n %d) #returns denominator and the remainder of numerator and denominator back to the function

def lowest_terms(n,d, gcd): #converts fraction into lowest terms 
    numerator = int(n/gcd) #divides numerator by gcd
    denominator = int(d/gcd) #divides denominator by gcd
    answer = (str(numerator) + "/" + str(denominator)) #final answer in "n/d" format
    return answer #returns answer 

def user_continue(): #if user wants to continue or not 
    while True: #loop
        try:
            option = input("Do you want to continue [Y/N]: ").lower()   #user choice 
            if option == "y" or option == "yes" or option == "n" or option == "no": #if choice is valid 
                break
            else:
                print("Enter a valid option [Y or N]") #if input is not valid 
        except:
            print("Enter a valid option [Y or N]") #if user input is not valid 
    return option   

def main(): #main function 
    while True: #while user wants to continue 
        fraction = user_input() #gets user input 
        gcd = greatest_common_divisor(fraction[0], fraction[1]) #finds greatest common denominator
        answer = lowest_terms(fraction[0], fraction[1], gcd) #gets the final answer
        print(f"{fraction[0]}/{fraction[1]} in lowest terms is {answer}") #prints resulsts
        choice = user_continue() #user choice (if they want to continue)
        if choice == "n" or choice == "no": #if user does not want to continue
            print("Thank you for using the program") 
            break #ends program
        
#main program        
if __name__ == "__main__":
	main()
