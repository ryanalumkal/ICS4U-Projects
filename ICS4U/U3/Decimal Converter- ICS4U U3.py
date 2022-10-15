# Name - Ryan Alumkal
# Grade - 12
# Description - Converts an integer (specified by user) to ascii, hexadecimal, or binary depending on what the user wants  
# Date -  October 14, 2022


#functions 
def user_choice(): #asks user what option they want to choose (between 1 and 4)
    while True:
        try:
            print("\n1. Convert to ASCII \n2. Convert to Hexadecimal \n3. Convert to Binary \n4. Exit")
            choice = int(input("Choose one of the following menu option (1-4): ")) #user input 
            if choice in range(1,5): #if choice is valid 
               break
            else:
                print("Enter a proper value between 1 and 4") #if choice in invalid 
        except:
            print("Enter a proper value between 1 and 4") #if choice in invalid 
     
    return choice #returns user choice to main program 

def number(): #asks user for an integer number 
    while True:
        try:
            num = int(input("Enter a integer number you wish to convert to from the previous choices: ")) 
            if num >0: #if number is valid
                break
            else:
                print("Enter a proper integer value over 0") #if choice in invalid
        except: 
            print("Enter a proper whole number value ") #if number is invalid 
    return num #returns user number to main program 

def ascii(num): #converts user number to ascii 
    print(f"\nThe ascii equivalent of {num} is {chr(num)}")
    
def hexadecimal(num): #converts user number to hexadecimal 
    print(f"\nThe hexadecimal equivalent of {num} is {hex(num)}")
    
def binary(num): #converts user number to binary 
    print(f"\nThe binary equivalent of {num} is {bin(num)}")
    
#main program
loop = True

while loop: #while user wants to use the program 
    choice = user_choice()
    if choice == 1: #if user wants ascii
        num = number()
        ascii(num) 
    elif choice == 2: #if user wants hexadecimal 
        num = number()
        hexadecimal(num)
    elif choice == 3: #if user wants binary 
        num = number()
        binary(num)
    elif choice == 4: #if user wants to quit program 
        loop = False
        print("Thank you for using this program")

#END 
