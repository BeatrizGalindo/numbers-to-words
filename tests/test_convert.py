import unittest
from src.convert import NumberToWordsConverter


class TestNumberToWords(unittest.TestCase):
    def test_zero(self):
        converter = NumberToWordsConverter(0)
        self.assertEqual(converter.number_to_words(), "zero")

    def test_single_digit(self):
        converter = NumberToWordsConverter(1)
        self.assertEqual(converter.number_to_words(), "one")
        converter = NumberToWordsConverter(9)
        self.assertEqual(converter.number_to_words(), "nine")

    def test_teens(self):
        converter = NumberToWordsConverter(11)
        self.assertEqual(converter.number_to_words(), "eleven")
        converter = NumberToWordsConverter(15)
        self.assertEqual(converter.number_to_words(), "fifteen")
        converter = NumberToWordsConverter(52)
        self.assertEqual(converter.number_to_words(), "fifty-two")

    def test_tens(self):
        converter = NumberToWordsConverter(20)
        self.assertEqual(converter.number_to_words(), "twenty")
        converter = NumberToWordsConverter(42)
        self.assertEqual(converter.number_to_words(), "forty-two")

    def test_hundreds(self):
        converter = NumberToWordsConverter(100)
        self.assertEqual(converter.number_to_words(), "one hundred")
        converter = NumberToWordsConverter(101)
        self.assertEqual(converter.number_to_words(), "one hundred and one")
        converter = NumberToWordsConverter(115)
        self.assertEqual(converter.number_to_words(), "one hundred and fifteen")
        converter = NumberToWordsConverter(352)
        self.assertEqual(converter.number_to_words(), "three hundred and fifty-two")
        converter = NumberToWordsConverter(999)
        self.assertEqual(converter.number_to_words(), "nine hundred and ninety-nine")

    def test_thousands(self):
        converter = NumberToWordsConverter(1000)
        self.assertEqual(converter.number_to_words(), "one thousand")
        converter = NumberToWordsConverter(12055)
        self.assertEqual(converter.number_to_words(), "twelve thousand and fifty-five")
        converter = NumberToWordsConverter(12300)
        self.assertEqual(converter.number_to_words(), "twelve thousand, three hundred")
        converter = NumberToWordsConverter(12345)
        self.assertEqual(converter.number_to_words(), "twelve thousand, three hundred and forty-five")
        converter = NumberToWordsConverter(99999)
        self.assertEqual(converter.number_to_words(), "ninety-nine thousand, nine hundred and ninety-nine")

    def test_exact_thousand(self):
        converter = NumberToWordsConverter(100000)
        self.assertEqual(converter.number_to_words(), "one hundred thousand")


if __name__ == "__main__":
    unittest.main()