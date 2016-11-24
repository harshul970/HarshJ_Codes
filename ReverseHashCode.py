letters ="acdegilmnoprstuw"

def HashFunction(x):

	ResultStr=""
	i=0
	b=8
	while b>7:
		a = x%37
		b = x/37
		if(a>15):
			ResultStr = ">gnirtS hsaH tcerrocnI<"
			break
		elif(b<7):			
			ResultStr = ">gnirtS hsaH tcerrocnI<"
			break
		ResultStr = ResultStr +letters[a]
		x=b
		i=i+1

	FinalString = ResultStr[::-1]
	return FinalString



HashString = 680131659347
print "String : "+HashFunction(HashString)
