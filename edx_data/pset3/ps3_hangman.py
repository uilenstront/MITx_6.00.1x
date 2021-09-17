# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    found = False

    for i in secretWord:
        if i not in lettersGuessed:
            return False
        else:
            found = True
    if found == True:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # g = ""
    # for i in secretWord:
    #     if i in lettersGuessed:
    #         g = g + i + " "
    #     else:
    #         g = g + "_ "
    # return g
    return ' '.join(['_' if l not in str(lettersGuessed) else l for l in secretWord])




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # string = 'abcdefghijklmnopqrstuvwxyz'
    # L = []
    # for i in string:
    #     if i not in lettersGuessed:
    #         L.append(i)
    # return ''.join(L)
    return ''.join([l for l in 'abcdefghijklmnopqrstuvwxyz' if l not in lettersGuessed])

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 8
    lettersGuessed = []

    while guesses_left >= 0:
        lettersGuessed.sort()

        if guesses_left == 8:
            guesses_left -= 1
            print("Welcome to the game Hangman!", "\n", "I am thinking of a word that is", len(secretWord), "letters long.")

        else:
            print("-------------")
            print("You have", guesses_left + 1, "guesses left")
            print("Available letters:", getAvailableLetters(lettersGuessed))

            guess = input("Please guess a letter: ")

            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess.lower())
                if guess in secretWord:
                    print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                    # guesses_left -= 1

                    if isWordGuessed(secretWord, lettersGuessed) == True:
                        print("-----------")
                        print("Congratulations, you won!")
                        break
                else:
                    print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                    guesses_left -= 1
                    if guesses_left < 0:
                        print("-------------", "\n", "Sorry, you ran out of guesses. The word was", secretWord)
                        break



secretWord = 'sea'
hangman(secretWord)