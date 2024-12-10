# Words for the basic numbers
ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"
MILLION = "million"

def number_to_words(number):
    # Handle specific case for 0
    if number == 0:
        return "zero"

    # Handle specific case for 100,000
    if number == 100000:
        return "one hundred thousand"

    # Split number into thousands and hundreds parts
    thousands_part = number // 1000
    remainder_part = number % 1000

    words = ""
    if thousands_part > 0:
        words += handle_hundreds(thousands_part) + " thousand"
        if 0 < remainder_part < 100:
            words += " and "
        elif 0 < remainder_part < 1000:
            words += ", "

    if remainder_part > 0:
        words += handle_hundreds(remainder_part)

    return words.strip()

def handle_hundreds(n):
    if n == 0:
        return ""
    elif n < 10:
        return ONES[n]
    elif 10 < n < 20:
        return TEENS[n - 10]
    elif n < 100:
        return TENS[n // 10] + ('' if n % 10 == 0 else '-' + ONES[n % 10])
    else:
        return ONES[n // 100] + " hundred" + ('' if n % 100 == 0 else ' and ' + handle_hundreds(n % 100))
