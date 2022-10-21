from words import words
import random
from random import choice

print("Ready to play Secret word?!")
print("-----------------------------")

words = ["About", "Audio", "Aware", "Aside", "Badly", "Black", "Birth", "Blame", "Baker", "Blood", "Cover", "China", "Civil", "Crash", "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime", "Codes", "Curve", "Cycle", "Guess", "Fruit", "Heavy", "Funny", "Night", "Grant", "Grand", "Giant", "Horse", "House",
         "Human", "Image", "Irony", "Juice", "Newly", "Media", "Might", "Nurse", "Occur", "Wound", "Water", "Yield", "Young", "Worth", "Voice"]
word = choice(words)     # randomly chooses a word from words list
guessed, chances, game_ends = [], 5, False  # multi variable assignment

# create a list of underscores to the length of the word
guesses = ["_"] * len(word)

# create a main loop
while not game_ends:
    hidden_word = "".join(guesses)
    print("Your guessed letters: {}".format(guessed))
    print("Word to guess: {}".format(hidden_word))
    print("Lives: {}".format(chances))
    ans = input("Type quit or guess a letter: ").lower()

    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
    elif ans in word and ans not in guessed:
        print("You guessed correctly!")
        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
    elif ans in guessed:
        print("You already guessed that. Try again")
    else:
        chances = -1
        print("Incorrect, you lost a chance")
    if ans not in guessed:
        guessed.append(ans)
    elif chances <= 0:
        print("You lost all your lives! The word was " + word)
        game_ends = True
    elif word == "".join(guesses):
        print("Congratulations, you guessed it correctly!")
        game_ends = True
