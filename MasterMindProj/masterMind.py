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
    actual_Array = convertToArray(actual);
    guess = getGuess();
    guess_Array = convertToArray(guess);
    turns = 1;
    while actual != getGuess:
        cows = [0, 0, 0, 0];
        cows = checkCows(actual_Array, guess_Array);
        bulls = [0, 0, 0, 0];
        bulls = checkBulls(actual_Array, guess_Array);
        print "Your guess generated " "cows and " bulls "bulls.";
        guess = getGuess();
        guess_Array = convertToArray(guess);
        turns = turns + 1;
    print "You guessed it! And it only too you " turns "!";

def checkCows(actual, guess):
