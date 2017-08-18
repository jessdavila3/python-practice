from random import randint

dieValue = randint(0, 9)
userGuess = input("What is your guess? ")

print "You guessed " + str(userGuess) + ". The die landed on " + str(dieValue) + "."