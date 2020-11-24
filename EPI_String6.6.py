def reverseWords(str):
	if len(str) == 0:
		return None
	str_list = str.split(" ")
	#Taking care of upper casing the first character of the last word as it is the one that occurs first in the final retuned string
	str_list[-1] = str_list[-1][0].upper()+ str_list[-1][1:] 
	return ' '.join(reversed(str_list))



print (reverseWords("Piggy is fat"))
