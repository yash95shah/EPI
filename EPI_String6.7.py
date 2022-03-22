def look_and_say(n):
	final_result = list()
	val = "1"
	def next_num(s):  #11
		i,count = 0,1
		ret = ''
		while i < len(s): 
			if i+1 < len(s) and s[i] == s[i+1]:
				count += 1
				i += 1
			ret += str(count)+ s[i]
			i += 1
		return ret

	for _ in range(n):
		final_result.append(val)
		val = next_num(val)

	return final_result[-1]


print (look_and_say(3))