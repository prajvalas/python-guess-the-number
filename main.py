#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from replit import clear
import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def play(number, attempts):
    while attempts > 0:
        attempts -= 1
        guess = int(input("Make a guess: "))
        if guess == number:
            print("CONGRATULATIONSSSSS HUMANNNN!")
            print(f"You got it! The number was {number}")
            return
        else:
            if guess > number:
                print("Too high.")
            else:
                print("Too low.")
            if attempts != 0:
                print("Guess again!")
                print(f"You have {attempts} remaining to guess the number.")
            else:
                print("OOPS! You've exhausted your attempts!")


def game_init():
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    level = input(
        "Choose a difficulty level. Type 'easy' or 'hard' : ").lower()
    attempts = 0
    if level == 'easy':
        attempts = EASY_LEVEL
        print("You have 10 attempts remaining to guess the number.")
    elif level == 'hard':
        attempts = HARD_LEVEL
        print("You have 5 attempts remaining to guess the number.")
    play(number, attempts)


flag = True
while flag:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    game_init()
    play_again = input("Play again? Type 'y or 'n' : ")
    if play_again == 'n':
        flag = False
        clear()
        print("Thanks for playing!")
    else:
        clear()
