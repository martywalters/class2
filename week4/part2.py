import re

def luhn_checksum(card_number):

    digits = [int(digit) for digit in card_number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total_sum = sum(digits)
    return (total_sum * 9) % 10

def validate_credit_card(card_number):

    card_number = card_number.replace(" ", "")  # Remove spaces
    #if not re.match(r"^\d{11,19}$", card_number):
    #    return False  # Invalid format (not a valid length or contains non-digits)
    check_digit = int(card_number[-1])
    #print('check digit: ' + str(check_digit))
    calculated_check_digit = luhn_checksum(card_number[:-1])
    return check_digit == calculated_check_digit

# Matches sequences of digits with optional spaces or hyphens
def find_credit_card_numbers(text):

    pattern = r"\b(?:\d[ -]*?){11,19}\b"  
    print(f"These values match CC regular express and will be passed to checksum validate\n{re.findall(pattern, text)}\n")
    return re.findall(pattern, text)


input_text = """Please use my credit card number. It is Visa #37562198673 with an expiration date of 08/19/2030. The CVS number is 854.
Please use my credit card number. It is test card #4111 1111 1111 1111  with an expiration date of 08/19/2030. The CVS number is 854.
Please use my credit card number. It is Visa #5431 1111 1111 1111  with an expiration date of 08/19/2030. The CVS number is 854.
Please use my credit card number. It is MasterCard #43711 1111 1111 114 with an expiration date of 08/19/2030. The CVS number is 854.
"""
credit_card_numbers = find_credit_card_numbers(input_text)

for card_number in credit_card_numbers:
    if validate_credit_card(card_number):
        print(f"Valid credit card number found: {card_number}")
    else:
        print(f"Invalid credit card number found: {card_number}")
