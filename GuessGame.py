# Guess game

def guessgame():
    """This method contains guess game using while loop """
    numberOfGuess=1
    print('WelCome To Number GuessGame, you have 7 attempts to complete the game:')
    while (numberOfGuess<=9):
        guess=int(input('Please enter your guess:'))
        if guess <50:
            print('You have entered a smaller number')
        elif guess > 50:
            print ('You have entered a bigger number')
        else:
            print('Congrats! You have Guessed Correctly!!!')
            print(numberOfGuess,' Number of guesses left before you finished')
            break
            print(7-numberOfGuess, 'Guesses Left Now!')
            numberOfGuess=numberOfGuess+1
            print(numberOfGuess)
    if (numberOfGuess > 9):
            print('Game Over, Max Number of Guess Exceeded!')
# Execute the function now
guessgame()
# The function has been executed successfully
