# Name - Ryan Alumkal
# Grade - 12
# Description - Uses user input and displays all prime numbers between 1 and the number  
# Date -  October 14, 2022

import math

#https://www.geeksforgeeks.org/prime-numbers/

def user_input():
    while True:
        try:
            num =int(input("Enter a integer number: "))
            if num > 0:
                break
            else:
                print("Enter a valid integer inputer greater than 0")
        except:
            print("Enter a valid integer number")
    return num

def num_type(num):
	if num ==1:
		return False
	for i in range(2,int(math.sqrt(num))+1):
		if (num%i == 0):
			return False
	return True


def prime_nums(num):
    value = []
    for i in range(1, num):
        for n in range(2,int(math.sqrt(i))+1):
            if (i%n == 0):
                break
            else:
                value.append(i)
    print(value)
    

#main 
num = user_input()
#type = num_type(num)
if num_type(num):
    print(f"The number {num} is a prime number")
    prime_nums(num)
else:
    print(f"The number {num} is not prime number")
    prime_nums(num)
