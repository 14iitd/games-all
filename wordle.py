import random


def generate_secret_word(word_list):
    return random.choice(word_list).upper()  # Choose a random word from the list and convert it to uppercase


def check_guess(secret_word, guess):
    if len(guess) != len(secret_word):
        return "Invalid guess length. Please guess a word with the same length as the secret word."

    guess = guess.upper()
    if guess == secret_word:
        return "Congratulations! You guessed the word!"

    feedback = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback += guess[i]  # Correct letter in correct position
        elif guess[i] in secret_word:
            feedback += '*'  # Letter is in the word but not in the correct position
        else:
            feedback += '-'  # Letter is not in the word at all
    return feedback


# List of words for the game
word_list = ['APPLE', 'ORANGE', 'LEMON', 'GRAPE', 'BANANA', 'CHERRY', 'MANGO']

# Generate a secret word
secret_word = generate_secret_word(word_list)

# Game loop
attempts = 5
while attempts > 0:
    print(f"\nAttempts left: {attempts}")
    guess = input("Enter your guess: ")
    result = check_guess(secret_word, guess)
    print(result)
    if result == "Congratulations! You guessed the word!" or attempts == 1:
        break
    attempts -= 1

if attempts == 0:
    print(f"\nOut of attempts! The secret word was: {secret_word}")
