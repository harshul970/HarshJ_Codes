letters = "acdegilmnoprstuw"    ##Output will contain only these letters

def hashConvert(hash_txt):		##Hash Function
	h=7
	i=0
	final_text = ""
	while i<h:
		ht = hash_txt[i]
		intht = int(ht)
		letter = letters[intht]
		final_text = final_text+letter
		i=i+1

	return final_text




hash_text ="930846109532517"
print hashConvert(hash_text)

##I didn't understand this question properly. So, based on my understanding i did it in this way.