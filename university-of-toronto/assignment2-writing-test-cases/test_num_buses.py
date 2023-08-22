import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """Test class for function a1.num_buses."""

    def test_exactly_50(self):
        """Test case for exactly 50 passengers, where only one bus is needed."""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_one_more_than_full_bus(self):
        """Test case for more than 50 passengers, requiring two buses."""
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)

    def test_one_less_than_full_bus(self):
        """Test case for less than 50 passengers, requiring only one bus."""
        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(expected, actual)

    def test_no_passengers(self):
        """Test case for 0 passengers, requiring no buses."""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
