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
        cows_Arr = [0, 0, 0, 0];
        cows_Arr = checkCows(actual_Array, guess_Array, cows_Arr);
        bulls_Arr = [0, 0, 0, 0];
        bulls_Arr = checkBulls(actual_Array, guess_Array, cows_Arr, bulls_Arr);
        cows = count(cows_Arr);
        bulls = count(bulls_Arr);
        print "Your guess generated " cows "cows and " bulls "bulls.";
        guess = getGuess();
        guess_Array = convertToArray(guess);
        turns = turns + 1;
    print "You guessed it! And it only too you " turns "!";

def convertToArray(num):
    convert = str(num);
    arr = [];
    for digit in num:
        arr.append(int(digit));
    return arr;

def checkCows(actual, guess, cows):
    num = 0;
    for digit in actual
