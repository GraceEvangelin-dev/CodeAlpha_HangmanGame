import random

# CodeAlpha Internship - Task 1
# Project: Hangman Game

# Step 1: Create a list of 5 words
words = ["python", "computer", "coding", "program", "developer"]

# Step 2: Select a random word
secret_word = random.choice(words)

# Step 3: Create underscores for the hidden letters
guessed_word = ["_"] * len(secret_word)

# Step 4: Store guessed letters
guessed_letters = []

# Step 5: Set the maximum incorrect guesses
max_guesses = 6
incorrect_guesses = 0

# Step 6: Display the game instructions
print("=" * 35)
print("         HANGMAN GAME")
print("=" * 35)
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses.")
print("")

# Step 7: Main game loop
while incorrect_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    if guessed_letters:
        print("Letters already guessed:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower().strip()

    # Step 8: Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter only one letter.")

    # Step 9: Check for repeated guesses
    elif guess in guessed_letters:
        print("You have already guessed that letter. Try again.")

    else:
        guessed_letters.append(guess)

        # Step 10: Check whether the guess is correct
        if guess in secret_word:
            print("Correct guess!")

            # Reveal every occurrence of the guessed letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess

        else:
            incorrect_guesses += 1
            print("Wrong guess!")

# Step 11: Display the final result
print("\n" + "=" * 35)

if "_" not in guessed_word:
    print("CONGRATULATIONS! YOU WON!")
    print("The correct word was:", secret_word)

else:
    print("GAME OVER! YOU LOST!")
    print("The correct word was:", secret_word)

print("=" * 35)
print("Thank you for playing Hangman!")