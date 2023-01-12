def factorial(nums): #calculates the sum of the different factorials
	if len(nums) == 1 and nums[0] ==0: #if user only inputs 0 as a number
		return 1
	else:
		sum = 0 #sum of factorials 
		for n in range (len(nums)-1): #checks every value  except 0
			factorials = 1 #resets value of factorials for every new value 
			for i in range(1, nums[n]+1): #calculates factorial
				factorials = i * factorials  #math
			sum += factorials #adds um of factorial
		return sum #returns sum
