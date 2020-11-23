def int_to_string(integer):
	out = list()
	is_neg = False
	if integer < 0:
		is_neg = True
		integer = -integer
	factor = 10

	while integer > 0:
		out.append(hex(integer%factor).replace('0x','').upper())
		integer //= factor
	print (out)
	if is_neg:
		sign = '-'
	else:
		sign = ''
	result = sign + ''.join(reversed(out))
	return result





def string_to_int(str):
	is_neg = str[0] == '-'
	factor = len(str[str[0]=="-":]) - 1
	result = 0
	for each in str[str[0]=="-":]:
		result += (ord(each) - ord('0')) * 10**factor
		factor -= 1
	if is_neg:
		result = - result
	return result


print(int_to_string(-328))
print(string_to_int("-328"))
