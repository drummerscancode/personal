import a1
import unittest

class TestNumBuses(unittest.TestCase):
	""" Test class for function a1.num_buses. 
	Tests whether the return value is int.
	Tests the low and high boundary for the input n.
	"""

	def test_num_buses_return_type(self):
		""" Tests whether the return type is of type int. """ 
		actual = a1.num_buses(50)
		assert isinstance(actual, int)


	def test_num_buses_low_boundary(self):
		""" Tests the lower boundary: 0. """
		actual = a1.num_buses(0)
		expected = 0
		self.assertEqual(expected, actual)	


	def test_num_buses_lower_than_boundary(self):
		""" Tests the lower than the boundary condition. """
		actual = a1.num_buses(49)
		expected = 1
		self.assertEqual(expected, actual)	


	def test_num_buses_boundary(self):
		""" Tests the boundary condition. """
		actual = a1.num_buses(50)
		expected = 1
		self.assertEqual(expected, actual)	


	def test_num_buses_larger_than_boundary(self):
		""" Tests the larger than the boundary condition. """
		actual = a1.num_buses(51)
		expected = 2
		self.assertEqual(expected, actual)	


	def test_num_buses_larger_than_boundary_2(self):
		""" Tests the larger than the boundary condition for bigger n. """
		actual = a1.num_buses(101)
		expected = 3
		self.assertEqual(expected, actual)	


if __name__ == '__main__':
    unittest.main(exit=False)
