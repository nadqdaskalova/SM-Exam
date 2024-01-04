import math
import unittest

def check_isfinite(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a valid number.")
    
    try:
        result = math.isfinite(number)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return False


class TestCheckIsFiniteFunction(unittest.TestCase):
    def test_finite_numbers(self):
        self.assertTrue(check_isfinite(42.0))
        self.assertTrue(check_isfinite(0))
        self.assertTrue(check_isfinite(-3.14))

    def test_infinite_numbers(self):
        self.assertFalse(check_isfinite(float('inf')))
        self.assertFalse(check_isfinite(float('-inf')))

    def test_nan(self):
        self.assertFalse(check_isfinite(float('nan')))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            check_isfinite('not a number')

    def test_complex_numbers(self):
        with self.assertRaises(TypeError):
            check_isfinite(3 + 4j)

if __name__ == '__main__':
    unittest.main()
