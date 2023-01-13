def factorial(num): #calculates the sum of the different factorials
	factorials = 1 #variable to hold value of factorial
	for i in range(1, num+1): #calculates factorial
		factorials = i * factorials  #math
	return factorials #returns sum
