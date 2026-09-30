import unittest
from tip_splitter import split_bill


class TestSplitBill(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(split_bill(100, 10, 2), 55.0)

    def test_no_tip(self):
        self.assertEqual(split_bill(90, 0, 3), 30.0)

    def test_one_person(self):
        self.assertEqual(split_bill(50, 20, 1), 60.0)

    def test_zero_people_fails(self):
        with self.assertRaises(ValueError):
            split_bill(100, 10, 0)

    def test_negative_total_fails(self):
        with self.assertRaises(ValueError):
            split_bill(-5, 10, 2)


if __name__ == "__main__":
    unittest.main()
