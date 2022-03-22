def display_valid_ips(s):
	def is_valid(str):
		if int(str) in range(255):
			return True

		else:
			return False


	part = [''] * 4
	outcome = list()
	for i in range(1, min(len(s),4)):
		part[0] = s[:i]
		if is_valid(part[0]):
			for j in range(1, min(len(s)-i, 4)):
				part[1] = s[i: i+j]
				if is_valid(part[1]):
					for k in range(1, min(len(s)-i-j,4)):
						part[2], part[3] = s[i+j:i+j+k], s[i+j+k:]
						if is_valid(part[2]) and is_valid(part[3]):
							outcome.append(part[0] + "." + part[1] + "." + part[2] + "." + part[3])
	return outcome


print (display_valid_ips("19216811"))

