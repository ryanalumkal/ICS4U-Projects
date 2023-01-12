# Name - Ryan Alumkal
# Grade - 12
# Description - States if a user-inputted number is within the exception of the standard deviation of a random value of 150 numbers
# Date -  December 5, 2022

#modules 
import random 

#user inputted number
def user_input():
    while True: #while input is invalid 
        try:
            value = int(input("Enter a number to calculate standard deviation: "))
            if value > 0: #if value is valid 
                return value
            else:
                print("Enter a correct value (Y/N)")
        except:
            print("Enter a correct value")	#if invalid 		

#calculates standard deviation of the random 150 values 
def standard_deviation(values): 
    #variables 
    num = 0
    value = 0
    squared_error = []

    #calculates average of numbers 
    for i in range(1,len(values)+1):
        num += values[i-1]
    u = num/len(values) #average
    #calculates squared error between data points and the average 
    for n in range(1,len(values)+1):
        squared_error.append((values[n-1]-u)**2)
    #finds average of the new value
    for m in range(1,len(squared_error)+1):
        value += squared_error[m-1]
    v = value/len(values) #average
    deviation = v **0.5 #final standard deviation

    return u, deviation #returns average of the values and standard deviation
    
def exception(u,deviation, value): #if the user-input is an exception or not
    if (u+deviation)> value > (u-deviation): #if value is not an exception
        print(f"Your value {value} is not an exception of {round(u,2)} with a standard deviation of {round(deviation,2)}")
    else: #if a value is an exception
        print(f"Your value {value} is an exception of {round(u,2)} with a standard deviation of {round(deviation,2)}")
        	
def main(): #main
    while True: #while user wants to continue 
        number = []
        for i in range (150): #random 150 numbers
            number.append(random.randint(25,75))
        value = user_input() #user input 
        nums = standard_deviation(number) #average of list number (num[0]) and standard deviation (num[1]) 
        exception(nums[0], nums[1], value) #finds if value is an exception 
        while True: #if user wants to end or continue program
            try:
                user_continue = input("Do you you want to continue (Y/N): ").lower()
                if user_continue == "y" or user_continue == "n": #if valid 
                    break
                else:
                    print("Enter a correct value (Y/N)")
            except:
                print("Enter a correct value (Y/N)")
        if user_continue == "n": #if user wants to end program
            print("Thank you for using the program")
            break

#main program
if __name__ == "__main__": 
    main()
