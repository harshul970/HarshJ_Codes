letters ="acdegilmnoprstuw"

def HashFunction(x):

	ResultStr=""
	i=0
	b=1
	while b!=7:
		a = x%37
		b = x/37
		ResultStr = ResultStr +letters[a]
		x=b
		i=i+1	

	FinalString = ResultStr[::-1]
	return FinalString



HashString = 680131659347
print "String : "+HashFunction(HashString)
