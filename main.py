import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 0

print(logo)

word = random.choice(word_list)
print(word)

placeholder = "_" * len(word)
print(f"Word to guess: {placeholder}")
print("\n*******************")

correct_letters = []

game_over = False

while not game_over:

    print(f"************* Number Of Errors {lives}/6 *************")

    guess = input("Guess a letter:  ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}!")

    display = ""

    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    
    if guess not in word:
        lives += 1
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        if lives == 6:
            game_over = True
            print(f"************* It was {word}! You lose *************")
            


    if "_" not in display:
        game_over = True
        print("You win!")
    
    print(stages[lives])