# from random_word import RandomWords
# r = RandomWords()
# print(r.get_random_word())
import random

r = RandomWords(WORDS)

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

print(random.choice(WORDS))

print("Ready to play Secret word?!")
print("----/////////---------//////////-------/////////------//////////----")


# def hangman(secretWord):
#     '''
#     secretWord: string, the secret word to guess.

#     Starts up an interactive game of Hangman.

#     * At the start of the game, let the user know how many
#       letters the secretWord contains.

#     * Ask the user to supply one guess (i.e. letter) per round.

#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the secret word.

#     * After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.
#   '''
#   pass
