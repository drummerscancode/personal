import a1
import unittest


class TestSwapK(unittest.TestCase):
	""" Test class for function a1.swap_k. 

	Consider first the list is a list of ints (dichotomy), then check the other types.
	Test the return type.
	Test the various sizes of the list (empty, one, two, smallest interesting, multiple items)
	in relation to the values for k (boundaries are 0 and len(L) // 2).

	"""
	
	def test_swap_k_return_value_is_NoneType(self):
		""" Tests whether the return value is really NoneType. """
		nums = [1, 2, 3]
		actual = a1.swap_k(nums, 1) 
		self.assertEquals(actual, None)


	def test_swap_k_empty_list(self):
		""" Tests the empty list. """
		nums = []
		a1.swap_k(nums, 0)
		expected = []
		self.assertEquals(nums, expected)


	def test_swap_k_one_item_list(self):
		""" Tests the one-element list: smallest odd possible. """
		nums = [1]
		a1.swap_k(nums, 0)
		expected = [1]
		self.assertEquals(nums, expected)


	def test_swap_k_two_item_list(self):
		""" Tests the two-element list: smallest even. """
		nums = [1, 2]
		a1.swap_k(nums, 1)
		expected = [2, 1]
		self.assertEquals(nums, expected)


	def test_swap_k_smallest_interesting_odd_items_low_boundary(self):
		""" Tests a list with a small number of odd number of items, with the low boundary for k. """
		nums = [1, 2, 3]
		a1.swap_k(nums, 0)
		expected = [1, 2, 3]
		self.assertEquals(nums, expected)
 

	def test_swap_k_smallest_interesting_odd_items_high_boundary(self):
		""" Tests a list with a small number of odd number of items, with the high boundary for k. """
		nums = [1, 2, 3]
		a1.swap_k(nums, 1)
		expected = [3, 2, 1]
		self.assertEquals(nums, expected)

	
	# Smallest interesting case with even items for low boundary does not add new info
	def test_swap_k_smallest_interesting_even_items_high_boundary(self):
		""" Tests a list with the smallest number of even number of items, with the high boundary for k. """
		nums = [1, 2, 3, 4]
		a1.swap_k(nums, 2)
		expected = [3, 4, 1, 2]
		self.assertEquals(nums, expected)

	
	# Testing with more odd items and the low boundary doesn't add new info.
	def test_swap_k_odd_items_high_boundary_k(self):
		""" Tests a list with an odd number of items, boundary for k = len // 2. """
		nums = [1, 2, 3, 4, 5]
		a1.swap_k(nums, 2)
		expected = [4, 5, 3, 1, 2]
		self.assertEquals(nums, expected)


	def test_swap_k_odd_items_between_boundary(self):
		""" Tests a list with an odd number of items, inbetween the boundaries for k. """
		nums = [1, 2, 3, 4, 5]
		a1.swap_k(nums, 1)
		expected = [5, 2, 3, 4, 1]
		self.assertEquals(nums, expected)


	def test_swap_k_even_items_high_boundary_k(self):
		""" Tests a list with an even number of items, boundary for k = len // 2. """
		nums = [1, 2, 3, 4, 5, 6]
		a1.swap_k(nums, 3)
		expected = [4, 5, 6, 1, 2, 3]
		self.assertEquals(nums, expected)


	def test_swap_k_even_items_between_boundary(self):
		""" Tests a list with an even number of items, inbetween the boundaries for k. """
		nums = [1, 2, 3, 4, 5, 6]
		a1.swap_k(nums, 2)
		expected = [5, 6, 3, 4, 1, 2]
		self.assertEquals(nums, expected)


	# If the items of the list are ints everything works ok. Check with other types too.
	def test_swap_k_odd_items_floats_between_boundary(self):
		""" Tests a list with an odd number of floats, inbetween the boundaries for k. """
		nums = [1.0, 2.0, 3.0, 4.0, 5.0]
		a1.swap_k(nums, 1)
		expected = [5.0, 2.0 , 3.0, 4.0, 1.0]
		for val1, val2 in zip(nums, expected):
			self.assertAlmostEquals(val1, val2)


	# What about strings?
	def test_swap_k_odd_items_strings_between_boundary(self):
		""" Tests a list with an odd number of strings, inbetween the boundaries for k. """
		nums = ['ab', 'cd', 'ef', 'gh', 'ij']
		a1.swap_k(nums, 1)
		expected = ['ij', 'cd' , 'ef', 'gh', 'ab']
		self.assertEquals(nums, expected)


	# and so on with other types.. maybe a list of lists?


if __name__ == '__main__':
	unittest.main(exit=False)
