
def map(str):
	if str is None:
		return -1
	else:
		return ord(str) -ord('A') + 1

def spreadsheet_convert(column_id):
	factor = len(column_id) -1 

	result = 0
	while factor>=0:
		for each in column_id:
			#print("Here")
			result += map(each) * (26**factor)
			factor -=1
	return result


print (spreadsheet_convert("EXTRAORDINARY"))