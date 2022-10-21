from words import words 
import random 



print("Ready to play Secret word?!")
print("-----------------------------")




# RandomWords(WORDS)




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


def game(x):
    wrong = 0
    # while not guessed and incorrect_guesses < 6:

    guessed_letter = input('Enter a letter\n')
    print(guessed_letter)

    if x in random_word:
        print("word is there")
        print_hangman(wrong)
    else:
        print(wrong)
        wrong = wrong + 1
        print("word is not there")
        print_hangman(wrong)


num_of_guesses = 6
guessed_corretly = False

# start of while loop
while num_of_guesses < 6 and not guessed_corretly:
    # get guess from player
    guess = input('Enter a 5 letter word and press enter: ')
    print('You have guessed', guess)
    num_of_guesses += 1

    guessed_corretly = num_of_guesses(guessed_corretly)


game("x")


def print_word(guess_letters):
    counter = 0
    correct_letters = 0
