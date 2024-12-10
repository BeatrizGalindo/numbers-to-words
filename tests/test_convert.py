import unittest
from src.convert import number_to_words


class TestNumberToWords(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(number_to_words(0), "zero")

    def test_single_digit(self):
        self.assertEqual(number_to_words(1), "one")
        self.assertEqual(number_to_words(9), "nine")

    def test_teens(self):
        self.assertEqual(number_to_words(11), "eleven")
        self.assertEqual(number_to_words(15), "fifteen")

    def test_tens(self):
        self.assertEqual(number_to_words(20), "twenty")
        self.assertEqual(number_to_words(42), "forty-two")

    def test_hundreds(self):
        self.assertEqual(number_to_words(100), "one hundred")
        self.assertEqual(number_to_words(101), "one hundred and one")
        self.assertEqual(number_to_words(999), "nine hundred and ninety-nine")

    def test_thousands(self):
        self.assertEqual(number_to_words(1000), "one thousand")
        self.assertEqual(number_to_words(12055), "twelve thousand and fifty-five")
        self.assertEqual(number_to_words(99999), "ninety-nine thousand, nine hundred and ninety-nine")

    def test_exact_thousand(self):
        self.assertEqual(number_to_words(100000), "one hundred thousand")


if __name__ == "__main__":
    unittest.main()
