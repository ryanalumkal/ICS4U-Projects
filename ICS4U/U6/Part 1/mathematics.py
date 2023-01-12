def factorial(nums):
	factorials = 1
	sum = 0
	for n in range (len(nums)):
		factorials = 1
		for i in range(1,nums[n]+1): #continues numbers till user number
			factorials = i * factorials  #math
		sum += factorials
	return (sum -1)