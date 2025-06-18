import random
from random import randint
max_attempts = 20

my_number = random.randint(1, 1000)

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= 1000:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, my_number):
            if guess == my_number:
                return "Correct!"
            elif guess > my_number:
                return "Sorry, that's too high!"
            else:
                return "Sorry, that's too low!"


def play_game():
    attempts = 0
    won = False
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, my_number)
        if result == "Correct!":
            print(f"Correct! \nThanks for playing, you win! You guessed the secret number in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result} \nTry again!")
    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {my_number}.")

if __name__ == "__main__":
    print("Welcome to number guesser!\nWhat's your name?")
    name = input("Name: ")
    print("Hello " + name + ". The rules of this game are simple, I'm going to pick a number between 1 and 1000, and your goal is to guess it!")
    print("I've picked a number between 1 and 100, now it's your turn to start guessing!")
    play_game()