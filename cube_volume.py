# Name: Nicholai Gallegos
# File: cube_volume.py
# Date: 2/7/2021

# Name: check_is_float
# Description: checks if input (a string) will convert to a valid float
# that is atleast 0.  If input is valid then returns True, it is is not
# valid then it returns False
def check_is_float(input):
	try:
		input = float(input)
		if input >= 0:
			return True
		else:
			return False
	except:
		return False

# Name: calculate_volume
# Description: Takes a side length (float) and raises it to the third power to
# calculate the volume of a cube of that side length.  Assumes good float 
# input.
def calculate_volume(side_length):
	return pow(float(side_length), 3)

# Name: run
# Description: Gets an input from the user, then calculates the volume of a
# cube from the side length given by the user
# ***Note*** this code runs, but the run() function is not called since it does
# not seem necessary for this assignment.
def run():
	good_input = False

	while good_input == False:
		vol = input("Enter side length: ")
		good_input = check_is_float(vol)

	print("Cube volume: " + str(calculate_volume(float(vol))) + " units") 

