
students = 38
probability = 1


for n in range(1,students+1):
    percentage = ((365-n+1)/365)
    probability = round((percentage * probability),2)

    if probability ==0.50:
        print(f"For a 50% probablity, {n} students are required")

 
solution = (1-probability)*100  
print(f"the probability that {n} students share the same birthday is {solution} %")