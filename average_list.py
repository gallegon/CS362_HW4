def valid_list(list):
	for i in list:
		try:
			i = int(i)
		except:
			return False
	return True

def list_average(list):
	sum = 0
	count = 0

	for i in list:
		sum += i
		count += 1
	
	return sum/count
