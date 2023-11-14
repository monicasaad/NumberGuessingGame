# import required modules
from art import logo
import random

# print logo and greeting
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")

# choose a random integer between 1 and 100 as answer
chosen_number = random.randint(1, 100)

# get user input for difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# set 10 lives for easy level and 5 lives for hard level
if difficulty == "easy":
    number_lives = 10
else:
    number_lives = 5

# let user keep guessing while they still have lives left
while number_lives > 0:

    # output to user current number of lives
    print(f"\nYou have {number_lives} attempts remaining to guess the number.")

    # get user input for guess
    guess = int(input("Make a guess: "))

    # output hint to user and take away a life or tell them if they got the answer
    if guess > chosen_number:
        print("\nToo high. Guess again.")
        number_lives -= 1
    elif guess < chosen_number:
        print("\nToo low. Guess again.")
        number_lives -= 1
    elif guess == chosen_number:
        print(f"\nYou got it! The answer was {chosen_number}.")
        # end asking for guess if the user got correct answer
        break

# tell user they lost if they run out of lives
if number_lives == 0:
    print("\nYou've run out of guesses. You lose.")
