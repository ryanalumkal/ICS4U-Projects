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
            for i in range (len(fraction)): #check each value of the fraction
                if fraction[i] == "/": #if a character is"/""
                    count_divide +=1 #add one to the count
                #checks if each value is an integer or not
                try: 
                    int(fraction[i]) #converts characters to integer
                except:
                    count_num +=1 #if a character is not an integer, add one to the count
                        
            if count_divide == 1: #if only one "/" exists
                if count_num == 1: #if only 1 invalid characters exists, the "/" in the user input
                    return fraction #if both conditions are true, return the value
        except: #if its not valid
            print("Enter a proper value")
    
def numbers(fraction): #returns the integers in the user input
    num = list(fraction.rstrip()) #coversts user input into a list
    n = "" #numerator
    d = "" #denominator
    for i in range (len(num)): #for the length of the list 
        if num[i] == "/": #checks where the "/" is 
            for y in range (i): #every characters before the "/"
                n += num[y] #adds it to the numerator string
            for m in range ((i+1), (len(num))): #every character after the "/"
                d += num[m] #adds it to the denominator string
    return int(n), int(d) #returns numerator and denominator as a integer

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
        values = numbers(fraction) #gets the numerator and denominator
        gcd = greatest_common_divisor(values[0], values[1]) #finds greatest common denominator
        answer = lowest_terms(values[0], values[1], gcd) #gets the final answer
        print(f"{fraction} in lowest terms is {answer}") #prints resulsts
        choice = user_continue() #user choice (if they want to continue)
        if choice == "n" or choice == "no": #if user does not want to continue
            print("Thank you for using the program") 
            break #ends program
        
#main program        
if __name__ == "__main__":
	main()
