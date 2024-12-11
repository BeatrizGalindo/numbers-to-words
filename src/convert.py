class NumberToWordsConverter:
    """
    A class to convert numbers into their English word representation.

    Attributes:
        number (int): The number to convert.
    """
    # Private constants for number-to-words mapping
    _ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    _TEENS = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    _TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    _HUNDRED = "hundred"
    _THOUSAND = "thousand"
    _MILLION = "million"

    def __init__(self,number):
        self.number = number

    def number_to_words(self):
        """
        Converts the number to its English word representation.

        Returns:
            str: The English word representation of the number.
        """

        # Handle specific case for 0
        if self.number == 0:
            return "zero"

        # Handle specific case for 100,000
        if self.number == 100000:
            return "one hundred thousand"

        # Split number into thousands and hundreds parts
        thousands_part = self.number // 1000
        remainder_part = self.number % 1000

        words = ""
        if thousands_part > 0:
            # Add words for thousands and handle remainder if needed
            words += self.handle_hundreds(thousands_part) + " thousand"
            if 0 < remainder_part < 100:
                words += " and "
            elif 0 < remainder_part < 1000:
                words += ", "

        if remainder_part > 0:
            # Add words for remainder
            words += self.handle_hundreds(remainder_part)

        return words.strip()

    def handle_hundreds(self, n):
        # Return empty string for 0
        if n == 0:
            return ""

        # For single-digit numbers, return the word from _ONES
        elif n < 10:
            return self._ONES[n]

        # For numbers between 11 and 19, return the word from _TEENS
        elif 10 < n < 20:
            return self._TEENS[n - 10]

        # For numbers between 20 and 99, return word from _TENS and handle ones if non-zero
        elif n < 100:
            return self._TENS[n // 10] + ('' if n % 10 == 0 else '-' + self._ONES[n % 10])

        # For numbers 100 and above, handle hundreds and recursively handle the remainder
        else:
            return self._ONES[n // 100] + " hundred" + ('' if n % 100 == 0 else ' and ' + self.handle_hundreds(n % 100))
