import random

userNum = int(input("Enter a number between 1-100: "))

# initialise variables
high = 100
low = 0
compGuess = random.randint(low, high)
correctGuess = False
 # not the most performance-optimised program, but it does the thing for now.

while correctGuess == False:
    userInput = input("Is your number " + str(compGuess) + "? (Higher/Lower/Y)")

    if userInput.lower() == "higher":
        # if userNum is higher, set low to computer's guess
        low = compGuess
        # compGuess becomes the average of low + high
        compGuess = (low + high)//2

    elif userInput.lower() == "lower":
        high = compGuess
        compGuess = (low + high)//2
    else:
        print("Your number was " + str(compGuess) + "!")
        correctGuess = True
        break
