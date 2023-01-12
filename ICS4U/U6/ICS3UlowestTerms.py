# Name - Ryan Alumkal
# Grade - 12
# Description - Returns a user-inputted fraction in lowest terms 
# Date -  

#Ask if user wants to continue 

def user_input():
	fraction = input("Enter a positive fraction in the format 'n/d': ")
	return fraction

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

def main():
    fraction = user_input()
    values = numbers(fraction)
    gcd = greatest_common_divisor(values[0], values[1])
    print(gcd)
    answer = lowest_terms(values[0], values[1], gcd)
    print(answer)
if __name__ == "__main__":
	main()