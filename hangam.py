import random

words = ["python", "computer", "programming", "developer", "database"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/ 6")

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
   