def countReplacedArray(arr):
	n = len(arr)
	write_idx, a_idx = 0, 0
	for i in range(n):
		if arr[i] != 'b':
			arr[write_idx] = arr[i]
			write_idx += 1
		if arr[i] == 'a':
			a_idx += 1


	current_idx = write_idx - 1
	write_idx += a_idx - 1

	while current_idx > 0:
		if arr[current_	idx] == 'a':
			arr[write_idx - 1 : write_idx + 1 ] = 'dd'
			write_idx -=1
		else:
			arr[write_idx] = arr[current_idx]
			write_idx -= 1
		cuurent_idx -= 1