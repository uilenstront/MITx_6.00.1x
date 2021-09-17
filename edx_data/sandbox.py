def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # g = ""
    #
    # for i in secretWord:
    #     if i in lettersGuessed:
    #         g = g + i + " "
    #     else:
    #         g = g + "_ "

    return ' '.join(['_' if l not in str(lettersGuessed) else l for l in secretWord])



secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))


'''
 return ''.join([l for l in 'abcdefghijklmnopqrstuvwxyz' if l not in lettersGuessed])
[unicode(x.strip()) if x is not None else '' for x in row]

'''