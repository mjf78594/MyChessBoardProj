from random import randint
def generateNum():
    actual = randint(0000, 9999);
    return actual;
def getGuess():
    guess = -1;
    while guess < 0 and guess >= 10000:
        guess = raw_input("Guess a number betweeen 0000 and 9999:"):
    return guess;
def main():
    actual = generateNum();
    guess = getGuess();
    while actual != getGuess:
        cows = checkCows(actual, guess);
        bulls = checkBulls(actual, guess);
        print "Your guess generated " "cows and " bulls "bulls.";
        guess = getGuess();
