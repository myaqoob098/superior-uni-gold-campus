import random

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def letter_guessing_game():
    word_list = ["python", "javascript", "hangman", "programming", "developer"]
    chosen_word = random.choice(word_list)
    guessed_letters = set()
    attempts = 5
    
    print("Welcome to the Letter Guessing Game!")
    print(f"The word has {len(chosen_word)} letters.")
    print(display_word(chosen_word, guessed_letters))
    print(f"You have {attempts} attempts to guess the letters.")

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in chosen_word:
            guessed_letters.add(guess)
            print(f"Good guess! {display_word(chosen_word, guessed_letters)}")
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print(f"Wrong guess. You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in chosen_word):
            print(f"Congratulations! You guessed the word: {chosen_word}")
            break

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct word was '{chosen_word}'.")

letter_guessing_game()
