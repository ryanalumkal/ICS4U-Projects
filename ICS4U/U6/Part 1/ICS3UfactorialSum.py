# Name - Ryan Alumkal
# Grade - 12
# Description - Calculates the sum of all factorials entered by a user
# Date -  



#Ask if user wants to continue 
#modules 
import mathematics

def user_input():
	nums = []
	while True:
		try:
			x = int(input("Enter a number: "))
			nums.append(x)
			if x == 0:
				return nums
				break
		except:
			print("Enter a proper value")
	
def main():
	nums = user_input()
	print(f"The sum of the factorials is {mathematics.factorial(nums)}")

#main program
if __name__ == "__main__": 
    main()