# Name - Ryan Alumkal
# Grade - 12
# Description - Simulates the roll of two dices and prints out the sum
# Date - September 20, 2022

import random

#variables 

dice_1 = random.randint(2,12) #Sum of the rolls of two dice (1A)
dice_2 = random.randint(1,6) #Dice roll (2A)
dice_3 = random.randint(1,6) #Dice roll (2A)

dice_sum = dice_2 + dice_3 #calculates sum of 2nd dice roll

print(f"The sum of the first dice roll is {dice_1}") #prints the results from the first dice roll
print(f"The sum of the second dice roll is {dice_sum}") #prints sum of dice roll 2

"""
Question 1C

The first dice roll is a random number between 2 and 12, meaning, there are no
numbers to add. The second dice roll calculates the sum of 2 different dices, meaning
that there are numbers to add; more variation. 

Roll 1 has a 1/11 (1 is not a possible value) chance of hitting any  value while the second 
roll has a 1/36 chance of hitting a any combination of values. 

The first roll has a 1/11 chance of hitting ANY sum (1 is not a possible sum); possibilites are equal.

The second roll has a higher chance of hitting values at the "beginning" and "end" values 
(ex: numbers 1-3 and 11-12 to have 2 specific combination of values) (ex 3: 1,2;2,1) (ex 12: 6,6;6,6)
"Middle" values have the lowest chance, (ex: numbers 4-10) (ex: 7: 3,4;4,3;6,1;1,6;2,5;5,2). 
Possibility varries. 



"""