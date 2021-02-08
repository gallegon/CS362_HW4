def first_last(first, last):
	if len(first) == 0 or len(last) == 0:
		return "error"
	else:
		full_name = str(first) + " " + str(last)
		return str(full_name)

print(first_last("Nick", ""))
