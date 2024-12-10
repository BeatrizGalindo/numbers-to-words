def number_to_words(number):
    if number < 0 or number > 100000:
        return "Number out of range. Please enter a number between 0 and 100,000."

    # Words for the basic numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Special case for zero
    if number == 0:
        return "zero"

    # Handle numbers from 1 to 99999
    if number == 100000:
        return "one hundred thousand"

    # Helper function for numbers less than 1000
    def handle_hundreds(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10])
        else:
            return ones[n // 100] + " hundred" + ('' if n % 100 == 0 else ' and ' + handle_hundreds(n % 100))

    # Split the number into thousands and hundreds part
    thousands_part = number // 1000
    remainder_part = number % 1000

    words = ""
    if thousands_part > 0:
        words += handle_hundreds(thousands_part) + " thousand"
        if 0 < remainder_part < 100:
            words += " and "
        elif 0< remainder_part < 1000:
            words += ", "

    if remainder_part > 0:
        words += handle_hundreds(remainder_part)

    return words.strip()
