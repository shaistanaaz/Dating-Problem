# Number of Male or Female 
N = 4

# This function returns true if 
# female 'f' prefers male 'm1' over male 'm' 
def fPrefersM1OverM(prefer, f, m, m1): 
	
	# Check if f prefers m over her 
	# currently dating m1 
	for i in range(N): 
		
		# If m1 comes before m in lisr of f, 
		# then f prefers her current date, 
		# don't do anything 
		if (prefer[f][i] == m1): 
			return True

		# If m cmes before m1 in f's list, 
		# then free her current date 
		# and set her date with m 
		if (prefer[f][i] == m): 
			return False

# Prints stable matching for N boys and N girls. 
# Boys are numbered as 0 to N-1. 
# Girls are numbereed as N to 2N-1. 
def DateCompatibility(prefer): 
	
	# Stores partner of female. This is our output 
	# array that stores paing information. 
	# The value of fPartner[i] indicates the partner 
	# assigned to female N+i. Note that the female numbers 
	# between N and 2*N-1. The value -1 indicates 
	# that (N+i)'th female is free 
	fPartner = [-1 for i in range(N)] 

	# An array to store availability of male. 
	# If mFree[i] is false, then male 'i' is free, 
	# otherwise engaged. 
	mFree = [False for i in range(N)] 

	freeCount = N 

	# While there are free males 
	while (freeCount > 0): 
		
		# Pick the first free male(we could pick any) 
		m = 0
		while (m < N): 
			if (mFree[m] == False): 
				break
			m += 1

		# One by one go to all female according to 
		# m's preferences. Here m is the picked free male 
		i = 0
		while i < N and mFree[m] == False: 
			f = prefer[m][i] 

			# The female of preference is free, 
			# f and m become partners (Note that 
			# the partnership maybe changed later). 
		
			if (fPartner[f - N] == -1): 
				fPartner[f - N] = m 
				mFree[m] = True
				freeCount -= 1

			else: 
				
				# If f is not free 
				# Find current engagement of wf
				m1 = fPartner[f - N] 

				# If w prefers m over her current engagement m1, 
				# then break the engagement between w and m1 and 
				# engage m with w. 
				if (fPrefersM1OverM(prefer, f, m, m1) == False): 
					wPartner[f - N] = m 
					mFree[m] = True
					mFree[m1] = False
			i += 1

			# End of Else 
		# End of the for loop that goes 
		# to all female in m's list 
	# End of main while loop 

	# Prthe solution 
	print("Female ", " Male") 
	for i in range(N): 
		print(i + N, "\t", fPartner[i]) 

# Driver Code 
prefer = [[7, 5, 6, 4], [5, 4, 6, 7], 
          [4, 5, 6, 7], [4, 5, 6, 7], 
          [0, 1, 2, 3], [0, 1, 2, 3], 
          [0, 1, 2, 3], [0, 1, 2, 3]] 
DateCompatibility(prefer) 


