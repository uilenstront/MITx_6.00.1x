def f(a, b):
    """
    a: int
    b: int
    should return one integer
    a = 1
    z = 26
    """
    return a + b


def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    # word in lowercase, it's no problem to do this (no difference between a and A)
    word = word.lower()

    # in short: put all letter values in one long list, then sort it
    scores = []

    for i in range(len(word)):                              # loop over the word
        letter = word[i]                                    # for each character in the word
        scores.append((ord(letter) - 96) * i)               # ord(letter) returnss the unicode number, if you -96 from this, you get the position in the alphabet
                                                            # simply take this value and * it times the position in the word (which is i)

    # sort the list
    scores.sort() # sort the list to get the highest values
    # scores.sort(reverse = True)

    return f(scores[-1], scores[-2]) # return the highest values from the list
    # return f(scores[0], scores[1])

print(score("abc", f))