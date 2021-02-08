import unittest
import name

class test_name(unittest.TestCase):
	def test_empty_input(self):
		self.assertEqual(name.first_last("",""), "error")
	def test_one_name_empty(self):
		self.assertEqual(name.first_last("Nick", ""), "error")
		self.assertEqual(name.first_last("", "Gallegos"), "error")
	def test_good_input(self):
		self.assertEqual(name.first_last("Nick", "Gallegos"), "Nick Gallegos")
	def test_bad_output(self):
		self.assertNotEqual(name.first_last("John", "Doe"), "JohnDoe")
		self.assertNotEqual(name.first_last("John", "Doe"), "John Doe ")

if __name__ == '__main__':
	unittest.main()
