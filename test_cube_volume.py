# Name: Nicholai Gallegos
# File: test_cube_volume.py
# Date: 2/7/2021

import unittest
import cube_volume

class test_cube_volume(unittest.TestCase):
	def test_check_is_float(self):
		self.assertEqual(cube_volume.check_is_float(-15), False)
		self.assertEqual(cube_volume.check_is_float(11), True)
	def test_string_input(self):
		self.assertEqual(cube_volume.check_is_float("string"), False)
		self.assertEqual(cube_volume.check_is_float(""), False)
	def test_calculate_volume(self):
		for i in range(10):
			self.assertEqual(cube_volume.calculate_volume(i), pow(i, 3))
		self.assertEqual(cube_volume.calculate_volume(13.3), pow(13.3, 3))

if __name__ == '__main__':
	unittest.main()
