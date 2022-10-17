# from random_word import RandomWords
# r = RandomWords()
# print(r.get_random_word())
import random


print("Ready to play Secret word?!")
print("-----------------------------")


word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

# RandomWords(WORDS)

random_word = random.choice(WORDS)


def game(x):
    wrong = 0
    # while not guessed and incorrect_guesses < 6:

    guessed_letter = input('Enter a letter')
    print(guessed_letter)

    if x in random_word:
        print("word is there")
    else:
        print(wrong)
        wrong = wrong + 1
        print(wrong)
        print("word is not there")


game("z")


def print_hangman(wrong):
    if (wrong == 0):
        print("\n+----+")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 1):
        print("\n+----+")
        print("O   |")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 2):
        print("\n+----+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n+----+")
        print(" 0  |")
        print("/|  |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 4):
        print("\n+----+")
        print(" 0  |")
        print("/|\ |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 5):
        print("\n+----+")
        print(" 0  |")
        print("/|\ |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif (wrong == 6):
        print("\n+----+")
        print(" O  |")
        print("/|\ |")
        print(" |  |")
        print("/   |")
    elif (wrong == 7):
        print("\n+----+")
        print(" O  |")
        print("/|\ |")
        print(" |  |")
        print("/ \ |")
        print("   ===")


print_hangman(0)


def print_word(guess_letters):
    counter = 0
    correct_letters = 0
