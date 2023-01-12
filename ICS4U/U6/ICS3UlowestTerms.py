# Name - Ryan Alumkal
# Grade - 12
# Description - Returns a user-inputted fraction in lowest terms 
# Date -  

#Ask if user wants to continue 

def user_input(): #Asks user for an input    
    while True:
        try:
            count_divide = 0
            count_num = 0
            fraction = input("Enter a positive fraction in the format 'n/d': ")
            for i in range (len(fraction)):
                if fraction[i] != "/":
                    count +=1
                #for n in range(10):
                    #if fraction[i] != (str(n)):
                       # print(n)
                        #count_num +=1
            if count_divide == len(fraction):
                #if count_num > 1:
                continue
            else:
                return fraction
        except:
            print("Enter a proper value")

def numbers(fraction):
    num = list(fraction.strip())
    n = ""
    d = ""
    for i in range (len(num)):
        if num[i] == "/":
            for y in range (i):
                n += num[y]
            for m in range ((i+1), (len(num))):
                d += num[m]
    return int(n), int(d)

def greatest_common_divisor(n, d):
    if (d == 0):
        return abs(n)
    else:
        return greatest_common_divisor(d, n %d)

def lowest_terms(n,d, gcd):
    numerator = int(n/gcd)
    denominator = int(d/gcd)
    answer = (str(numerator) + "/" + str(denominator))
    return answer

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

def main():
    while True:
        fraction = user_input()
        values = numbers(fraction)
        gcd = greatest_common_divisor(values[0], values[1])
        print(gcd)
        answer = lowest_terms(values[0], values[1], gcd)
        print(f"{fraction} in lowest terms is {answer}")
        choice = user_continue() #user choice (if they want to continue)
        if choice == "N" or choice == "n": #if user does not want to continue
            print("Thank you for using the program") 
            break #ends program
if __name__ == "__main__":
	main()