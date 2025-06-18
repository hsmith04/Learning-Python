import random


def scramble_word(word):
    return "".join(random.sample(word, len(word)))

words = [
    "python", "programming", "developer", "algorithm", "function",
    "variable", "syntax", "debugging", "iteration", "recursion",
    "software", "hardware", "keyboard", "monitor", "internet",
    "database", "framework", "library", "compiler", "runtime",
    "binary", "network", "encryption", "virtual", "machine",
    "array", "string", "integer", "boolean", "exception",
    "module", "package", "object", "inheritance", "polymorphism",
    "dictionary", "tuple", "loop", "condition", "parameter"
]
word = random.choice(words)
scrambled = scramble_word(word)

print("Scrambled word:", scrambled)

def game_play(word):
    attempts = 3
    while attempts > 0:
       guess = input("Guess the word: ").lower()
       if guess == word:
           print("Correct!")
           break
       else:
           attempts -= 1
           print(f"Wrong! {attempts} attempt(s) left.")
    if attempts == 0:
       print(f"Game over! The correct word was {word}.")

def menu():
    while True:
        word = random.choice(words)
        scrambled = scramble_word(word)
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y":
            print("Scrambled word:", scrambled)
            game_play(word)
        elif play_again != "y" and play_again != "n":
            print("Invalid input. Try again.")
        else:
            break

if __name__ == '__main__':
    game_play(word)
    menu()
