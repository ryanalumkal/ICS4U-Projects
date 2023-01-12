# Name - Ryan Alumkal
# Grade - 12
# Description - Calculates the sum of all factorials entered by the user
# Date -  1/12/2023

#modules 
import calculations

def user_input(): #asks user for input
	nums = [] #numbers in a list 
	while True:
		try: #checks if user input is correct
			x = int(input("Enter a number (enter 0 to stop): ")) #asks user input
			if x >= 0: #if value is greater or equal to 0 (equal to 0 used when user only inputs 0 and no other value)
				nums.append(x) #adds to the list "nums"
			elif x < 0: #if value is 0 or less 
				print("Enter a correct input")
			if x == 0: #if value is 0
				return nums
				break
		except:
			print("Enter a proper value")
			
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
	while True:
		nums = user_input() #gets the user input 
		print(f"The sum of the factorials is {calculations.factorial(nums)}") #ouputs user input using a module from calculations.py (attached file)
		choice = user_continue() #user choice (if they want to continue)
		if choice == "n" or choice == "no": #if user does not want to continue
			print("Thank you for using the program") 
			break #ends program

#main program
if __name__ == "__main__": 
    main()
