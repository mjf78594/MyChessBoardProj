from random import randint
def generateNum():
    actual = randint(0000, 9999);
    return actual;
def getGuess():
    guess = -1;
    while guess < 0 and guess >= 10000:
        guess = raw_input("Guess a number betweeen 0000 and 9999:"):
    return guess;
