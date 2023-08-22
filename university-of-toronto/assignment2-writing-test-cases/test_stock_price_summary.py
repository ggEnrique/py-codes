import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """Test class for function a1.stock_price_summary."""

    def test_mixed_price_changes(self):
        """Test case for a list of mixed positive, negative, and zero price changes."""
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)

    def test_single_price_change_positive(self):
        """Test case for a list with a single positive price change."""
        actual = a1.stock_price_summary([0.01])
        expected = (0.01, 0)
        self.assertEqual(actual, expected)

    def test_single_price_change_negative(self):
        """Test case for a list with a single negative price change."""
        actual = a1.stock_price_summary([-0.01])
        expected = (0.01, 0)
        self.assertEqual(actual, expected)

    def test_all_zero_price_changes(self):
        """Test case for a list where all price changes are zero."""
        actual = a1.stock_price_summary([0, 0, 0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_only_positive_changes(self):
        """Test case for a list where all price changes are positive."""
        actual = a1.stock_price_summary([0.01, 0.03, 0.05])
        expected = (0.09, 0)
        self.assertEqual(actual, expected)

    def test_only_negative_changes(self):
        """Test case for a list where all price changes are negative."""
        actual = a1.stock_price_summary([-0.01, -0.03, -0.05])
        expected = (0, -0.09)
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """Test case for an empty list."""
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(exit=False)
