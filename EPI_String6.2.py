def convertBase(str, b1, b2):
	decimal_value = convertDecimal(str,b1)
	#print (decimal_value)
	output = list()
	while decimal_value >0:
		print (hex(decimal_value % b2))
		output.append(hex(decimal_value % b2).replace('0x', '').upper())
		decimal_value = decimal_value // b2
	result = ''.join(reversed(output))
	return result


def convertDecimal(str, b1):
	factor = len(str) - 1
	temp_result = 0
	for each in str:
		temp_result += (ord(each)- ord('0')) * b1**factor
		factor -= 1
	return temp_result



print(convertBase("615",7,13))