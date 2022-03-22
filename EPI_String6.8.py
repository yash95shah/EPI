def roman_to_integer(s):
	val = 0
	t = list()
	for cha in s:
		t.append(conv.get(cha))
	

	for i in reversed(range(len(t))):
		#print(i)
		if t[i] >  t[i-1] and i>0:
			val += t[i]- t[i-1] 
		elif t[i] == t[i-1] and i == len(t)-1:
			val += 2* t[i]
		elif t[i] <= t[i-1] and i>0:
			val += t[i-1]

		# else:
		# 	val += t[i] - t[i-1]
		#print (val)
		
	return val



conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 500}


print (roman_to_integer("LVIIII"))