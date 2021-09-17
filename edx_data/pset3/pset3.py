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