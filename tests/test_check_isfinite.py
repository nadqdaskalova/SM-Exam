import unittest
from isfinite import check_isfinite


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