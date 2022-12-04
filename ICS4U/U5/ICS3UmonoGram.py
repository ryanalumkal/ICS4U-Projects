# Name - Ryan Alumkal
# Grade - 12
# Description - Prints a monogram from a user-specified name
# Date -  December 5, 2022

def monogram(name): #find monogram 
	#assigns values of the name to different variables: first, last, and middle
	first_name = name[0] 
	last_name = name[2]
	middle_name = name[1]
	#changes the first value of the name to lower (first and middle), and upper (last)
	first_initial = first_name[0].lower()
	last_initial = last_name[0].upper()
	middle_initial = middle_name[0].lower()
	name_monogram = first_initial + last_initial + middle_initial #monogram
	return name_monogram

def main():
	while True: #while user wants to continue 
		while True: #while user name is invalid
			try:
				user_name = input("Enter your full name (first, middle, last): ")
				name = user_name.split()
				if len(name) == 3: #if user name has 3 words (first, middle, and last)
					break #continue 
				else:
					print("Enter a correct value")  #if invalid 
			except:
				print("Enter a valid name")
		name_monogram = monogram(name) #finds monogram
		print(f"The monogram of {user_name} is {name_monogram}") #prints monogram
		while True: #if user wants to continue 
			try:
				user_continue = input("Do you you want to continue (Y/N): ").lower()
				if user_continue == "y" or user_continue == "n": #if user continue is valid 
					break
				else:
					print("Enter a correct value (Y/N)")
			except:
				print("Enter a correct value (Y/N)") #if invalid 
		if user_continue == "n": #if user wants to stop
			print("Thank you for using the program")
			break	

#main program			
if __name__ == "__main__":
	main()