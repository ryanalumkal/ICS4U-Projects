# Name - Ryan Alumkal
# Grade - 12
# Description - 
# Date -  October 31, 2022

def factorial(n): #calculates factorial
    factorials =1 #starts of at 1
    for i in range(1,n+1): #continues numbers till user number
        factorials = i *factorials  #math
    return factorials #returns factorial

def get_n(): #user input
    while True:
        try:
            n = int(input("Enter a number:")) #gets user input
            if n >0:
                return n #if valid
            else:
                print("Enter a valid integer number greate than 0") #if invalid 
        except:
            print("Enter a valid integer number") #if invalid 

def output(n, factorials): #outputs factorial 
    print(f"The factorials of {n} is {factorials}")

def user_continue(): #if user wants to continue or not 
    while True: #loop
        try:
            option = str(input("Do you want to continue [Y/N]: "))   #user choice 
            if option == "Y" or option == "y" or option == "N" or option == "n": #if choice is valid 
                break
            else:
                print("Enter a valid option [Y or N]") #if input is not valid 
        except:
            print("Enter a valid option [Y or N]") #if user input is not valid 
    return option    

def main(): #main function 
    while True: 
        n = get_n() #user input
        factorials = factorial(n) #calculates factorial
        output(n, factorials) #outputs factorial 
        choice = user_continue() #user choice (if they want to continue)
        if choice == "N" or choice == "n": #if user does not want to continue 
            break
if __name__ == '__main__': 
    main()
    
