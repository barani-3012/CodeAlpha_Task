import random

def get_random_word():
    word_list = ["python", "hangman", "challenge", "programming", "computer", "keyboard"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman_game():
    word = get_random_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman_game()
