# Name - Ryan Alumkal
# Grade - 12
# Description - Calculates the probability of 2 peope sharing the same birtday in a room and the # of people needed for for a 50% probability 
# Date -  September 27, 2022

students = 38 # number of students in a room 
probability = 1 #starting probability; 100% 


for n in range(1,students+1): # calculates percentage from # of students 1-38
    percentage = ((365-n+1)/365) #equation
    probability = round((percentage * probability),2) #final percentage depending on students 

    if probability ==0.50: #when probability is 50% 
        print(f"For a 50% probablity, {n} students are required") #prints results (students required) 

 
solution = (1-probability)*100  #final solution
print(f"the probability that {n} students share the same birthday is {solution} %") #prints final solution 