import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
	""" Test class for function a1.stock_price_summary. 

	The main categories tested are size: empty, one-element, smallest interesting case and multiple items
	and dichotomies: zero, positive, negative items.
	
	An additional dichotomy could be testing the different numeric types: int, float or long - a stock can't have a complex price I suppose ;), but the tests below would catch these errors too.
	The boundary value is 0 (considered already) and order of the items does not affect results since the sum is commulative (and besides order can be considered as tested while testing the various dichotomies).

	"""

	def test_stock_price_summary_return_type(self):
		""" Tests that the return type of the method is a tuple. """
		actual = a1.stock_price_summary([0.01, -0.03])
		assert isinstance(actual, tuple) 
		

	def test_stock_price_summary_number_of_return_values(self):
		""" Tests whether the inner items of the tuple are 2. """
		import numbers # Python 2.6+ 
		actual = a1.stock_price_summary([0.01, -0.03])
		assert (len(actual) == 2), "Return value does not have 2 items."


	def test_stock_price_summary_empty_list(self):
		""" Tests the empty list. """
		actual = a1.stock_price_summary([])
		expected = (0, 0)
		self.custom_test(actual, expected)
	
	
	def test_stock_price_summary_one_item_zero(self):
		""" Tests a list with a single item, 0. """
		actual = a1.stock_price_summary([0])
		expected = (0, 0)
		self.custom_test(actual, expected)


	def test_stock_price_summary_one_item_positive(self):
		""" Tests a list with a single item, > 0. """
		actual = a1.stock_price_summary([1])
		expected = (1.00, 0)
		self.custom_test(actual, expected)


	def test_stock_price_summary_one_item_negative(self):
		""" Tests a list with a single item, < 0. """
		actual = a1.stock_price_summary([-1])
		expected = (0, -1)
		self.custom_test(actual, expected)


	def test_stock_price_summary_multiple_items_zero(self):
		""" Tests a list with multiple items, all 0. """
		actual = a1.stock_price_summary([0, 0.0])
		expected = (0, 0)
		self.custom_test(actual, expected)


	def test_stock_price_summary_multiple_items_positive(self):
		""" Tests a list with multiple items, all > 0. """
		actual = a1.stock_price_summary([0.01, 0.02, 0.03])
		expected = (0.06, 0)
		self.custom_test(actual, expected)


	def test_stock_price_summary_multiple_items_negative(self):
		""" Tests a list with multiple items, all < 0. """
		actual = a1.stock_price_summary([-0.02, -0.03])
		expected = (0, -0.05)
		self.custom_test(actual, expected)

	
	def test_stock_price_summary_smallest_interesting_case(self):
		""" Tests a list with one item in each category. """
		actual = a1.stock_price_summary([0.02, 0, -0.03])
		expected = (0.02, -0.03)
		self.custom_test(actual, expected)


	def test_stock_price_summary_multiple_items_mixed(self):
		""" Tests a list with multiple items, that are mixed. """
		actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
		expected = (0.14, -0.17)
		self.custom_test(actual, expected)


	def custom_test(self, actual, expected):
		""" This custom test method is introduced to assertAlmostEquals for every float of the result(tuple). 
		Note that assertAlmostEquals also (internally) checks that the values are numbers
		
		"""
		for val1, val2 in zip(expected, actual): # will throw if not iterables, but you can't tell that they are tuples, this is why we introduced the first test_return_type
			self.assertAlmostEquals(val1, val2, 7) # will also throw TypeError if any of the values is not a number


if __name__ == '__main__':
    unittest.main(exit=False)
