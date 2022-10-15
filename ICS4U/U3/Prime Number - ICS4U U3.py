# Name - Ryan Alumkal
# Grade - 12
# Description - Uses user input and displays all prime numbers between 1 and the number  
# Date -  October 14, 2022

import math

def user_input(): #user input 
    while True:
        try:
            num =int(input("Enter a integer number: "))
            if num > 0: # if user input is valid, break 
                break
            else: #if user input is less than or equal to 0 
                print("Enter a valid integer inputer greater than 0")
        except: #if user input is not a string 
            print("Enter a valid integer number")
    return num # returns user num

def num_type(num): #check type of num 
	if num ==1: #only for 1
		return False #number is not prime
	for i in range(2,int(math.sqrt(num))+1): #checks if every number in between is divisiable by the original number or not 
		if (num%i == 0):
			return False #number is not prime 
	return True #if none of the above is true, number is prime 

def prime_nums(num): #checks all values between the number
    value = [] #value array/list
    for i in range (1, num+1): #loops through all the numbers in between 1 and the number 
        type = num_type(i) #type (prime or not)
        if type:
            value.append(i) #if number is prime, add to list 
    return value

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
    
#main 
while True: #main loop 
    num = user_input() #user number 
    #type = num_type(num)
    if num_type(num): #if number is prime 
        print(f"The number {num} is a prime number")
        print(f"The prime numbers between 1 and {num} is {prime_nums(num)}")
    else: #if number is not prime 
        print(f"The number {num} is not prime number")
        print(f"The prime numbers between 1 and {num} is {prime_nums(num)}")
    choice = user_continue() #user choice if they want to continue or not 
    if choice == "N" or choice == "n": #if user does not want to continue, stop, else, continue 
        break

#END 