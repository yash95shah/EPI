def isPalindrome(str):
	if str is None or len(str)==0:
		return -1
	for char_index in range(len(str)//2):
		if str[char_index] != str[-char_index-1]:
			return False

	return True




print(isPalindrome("abas"))