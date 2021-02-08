import unittest
import average_list

class test_average_list(unittest.TestCase):
	def test_valid_list(self):
		self.assertTrue(average_list.valid_list([3,4,5]))
	def test_invalid_list(self):
		self.assertFalse(average_list.valid_list([3, 4, "fifteen"]))
	def test_average_list(self):
		self.assertEqual(average_list.list_average([4, 6, 12, 18]), 10)
		self.assertEqual(average_list.list_average([15, 5, 37, 3]), 15)
		self.assertEqual(average_list.list_average([-3, 3, 12]), 4)
		self.assertEqual(average_list.list_average([-3, 3, 12]), 4)
	@unittest.expectedFailure
	def test_fail(self):
		self.assertEqual(average_list([3, 4,5, 67]), 30)
		self.assertEqual(average_list([]), 0)	

if __name__ == '__main__':
	unittest.main()
