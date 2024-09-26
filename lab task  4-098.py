def luhn_check(card_number):
    """Checks if a card number is valid using the Luhn algorithm.

    Args:
        card_number (str): The card number to check. It must be a string of digits.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """

    if not card_number.isdigit():
        return False

    
    digits = list(map(int, card_number))

    
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        digits[i] = doubled - 9 if doubled > 9 else doubled

    total_sum = sum(digits)

    
    return total_sum % 10 == 0



card_number = input("Enter a card number to validate: ")
if luhn_check(card_number):
    print("The card number is valid.")
else:
    print("The card number is invalid.")






### Task 2
def remove_digits(string):
    """Removes digit characters from a string.

    Args:
        string: The input string.

    Returns:
        The string without digits.
    """

    result = ""
    for char in string:
        if not char.isdigit():
            result += char
    return result






### TASK 3
def sort_words_by_length(text):
    """Sorts words in a string by their length.

    Args:
        text: The input string.

    Returns:
        A list of words sorted by length.
    """

    words = text.split()
    sorted_words = []
    while words:
        min_word = words[0]
        min_index = 0
        for i in range(1, len(words)):
            if len(words[i]) < len(min_word):
                min_word = words[i]
                min_index = i
        sorted_words.append(min_word)
        words.pop(min_index)
    return sorted_words


