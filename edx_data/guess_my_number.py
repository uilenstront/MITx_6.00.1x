low = 0
high = 100

print("Please think of a number between 0 and 100!")

while True:
    guess = int((low + high) / 2)
    response = input("Is your secret number " + str(guess) + "?\n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == 'l': # this would mean the low needs to be higher
        low = guess
    elif response == 'h': # this would mean the high needs to be lower
        high = guess
    elif response == 'c':
        print("Game over. Your secret number was: ", guess)
        break
    else:
        print("Sorry, I did not understand your input.")


