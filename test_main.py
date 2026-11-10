import unittest

from main import add_numbers


class AddNumbersTests(unittest.TestCase):
	def test_positive_numbers(self):
		self.assertEqual(add_numbers(2, 3), 5)

	def test_negative_numbers(self):
		self.assertEqual(add_numbers(-2, -3), -5)

	def test_mixed_numbers(self):
		self.assertEqual(add_numbers(-2, 5), 3)


if __name__ == "__main__":
	unittest.main()
