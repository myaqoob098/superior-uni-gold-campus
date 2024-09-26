def custom_sequence(number, rules):
    """
    Generates a sequence based on custom rules for divisors.
    
    Parameters:
    - number: The upper limit of the sequence.
    - rules: A dictionary where keys are divisors and values are the words to print.
    
    Returns:
    - A list of strings representing the custom sequence.
    """
    result = []
    for num in range(1, number + 1):
        output = ""
        for divisor, word in rules.items():
            if num % divisor == 0:
                output += word
        if not output:  
            output = str(num)
        result.append(output)
    return result


try:
    number = int(input("Enter the upper limit for the Custom Sequence Game: "))
    
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        rules = {}
        print("Define your custom rules:")
        while True:
            divisor = input("Enter a divisor (or type 'done' to finish): ").lower()
            if divisor == 'done':
                break
            try:
                divisor = int(divisor)
                if divisor <= 0:
                    print("Please enter a positive integer for the divisor.")
                    continue
                word = input(f"Enter the word for multiples of {divisor}: ")
                rules[divisor] = word
            except ValueError:
                print("Invalid input. Please enter a positive integer for the divisor.")

        
        custom_sequence_result = custom_sequence(number, rules)
        
        print("\nCustom Sequence Output:")
        print("\n".join(custom_sequence_result))

except ValueError:
    print("Invalid input. Please enter a positive integer.")
