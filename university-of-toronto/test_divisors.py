import unittest
import divisors


class TestDivisors(unittest.TestCase):
    def test_divisors_1(self):
        actual = divisors.get_divisors(8, [1, 2, 3])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_divisors_2(self):
        actual = divisors.get_divisors(12, [0, 1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(exit=False)