import random
from random import choice

correctGuess = False

userNum = int(input("Enter a number between 1-100: "))

previousGuesses = []

compGuess = choice([i for i in range(0,100) if i not in previousGuesses]) # computer chooses number between 1-100
# however, we want the computer not to repeat the numbers it previously chose
# does this actually work? Not quite. I will do more investigating.


while correctGuess == False:
    userInput = input("Is your number " + str(compGuess) + "? (Higher/Lower/Y)")

    if userInput == "Higher":
        newGuess = random.randint(compGuess, 100)
        previousGuesses.append(newGuess)
        compGuess = newGuess

    elif userInput == "Lower":
        newGuess = random.randint(1, compGuess)
        previousGuesses.append(newGuess)
        compGuess = newGuess
    else:
        newGuess = compGuess
        print("Your number was " + str(newGuess) + "!")
        correctGuess == True
        break