import a1
import unittest

class TestSwapK(unittest.TestCase):
    """Test class for function a1.swap_k."""

    def test_swap_two_elements(self):
        """Test case for swapping the first two and last two elements."""
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(nums, expected)

    def test_swap_one_element(self):
        """Test case for swapping the first and last element."""
        nums = [1, 6, 7]
        a1.swap_k(nums, 1)
        expected = [7, 6, 1]
        self.assertEqual(nums, expected)

    def test_swap_strings(self):
        """Test case for swapping the first two and last two strings."""
        nums = ["a", "b", "c", "d"]
        a1.swap_k(nums, 2)
        expected = ["c", "d", "a", "b"]
        self.assertEqual(nums, expected)

    def test_empty_list(self):
        """Test case for an empty list."""
        nums = []
        a1.swap_k(nums, 0)
        expected = []
        self.assertEqual(nums, expected)


    def test_swap_zero_elements(self):
        """Test case for swapping zero elements."""
        nums = [1, 2, 3, 4]
        a1.swap_k(nums, 0)
        expected = [1, 2, 3, 4]
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main(exit=False)
