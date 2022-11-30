# Name - Ryan Alumkal
# Grade - 12
# Description - 
# Date -  December 1, 2022

import random 
import math
#lists
number = []
squared_error = []


def user_input():
    value = int(input("Enter a number to calculate standard deviation: "))
    return value

def standard_deviation(x):
    num = 0
    value = 0
    #print(x)
    for i in range(1,len(x)+1):
        #print(i)
        num += x[i-1]
    u = num/len(x) #average
    #print(u)
    for n in range(1,len(x)+1):
        squared_error.append((x[n-1]-u)**2)
    for m in range(1,len(squared_error)+1):
        value += squared_error[m-1]
    v = value/len(x)
    deviation = v **0.5
    """ # way to check deviation, simplify code above
    mean = sum(x) / len(x)
    variance = sum([((k - mean)**2) for k in x]) / len(x)
    res = variance ** 0.5
    print(res)
    """
    return u, deviation
    
def exception(u,deviation, value):
    if value > (u+deviation)  or  value < (u-deviation):
        print(f"Your value {value} is an exception of {u} with a standard deviation of {deviation}")
    else:
        print(f"Your value {value} is not an exception of {u} with a standard deviation of {deviation}")
def main():
    for i in range (150):
        number.append(random.randint(25,75))
    value = user_input()
    nums = standard_deviation(number) 
    exception(nums[0], nums[1], value)

#main
if __name__ == "__main__": 
    main()