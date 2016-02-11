from random import randint

def generateNum():
    actual = randint(0000, 9999)
    return actual

def getGuess():
    guess = -1
    while guess < 0 and guess >= 10000:
        guess = raw_input("Guess a number betweeen 0000 and 9999:")
    return guess

def main():
    actual = generateNum()
    actual_Array = convertToArray(actual)
    guess = getGuess()
    guess_Array = convertToArray(guess)
    turns = 1
    while actual != getGuess:
        cows_Arr = checkCows(actual_Array, guess_Array)
        bulls = checkBulls(actual_Array, guess_Array, cows_Arr)
        cows = countCows(cows_Arr)
        print "Your guess generated " + cows + "cows and " + bulls + "bulls."
        guess = getGuess()
        guess_Array = convertToArray(guess)
        turns = turns + 1;
    print "You guessed it! And it only too you " + turns + "!"

def convertToArray(num):
    convert = str(num)
    arr = []
    for digit in convert:
        arr.append(digit)
    return arr

def countCows(arr):
    i = 0
    for binum in arr:
        if arr[binum] == 1:
            i = i + 1
    return i

def checkCows(actual, guess):
    cows = []
    for digit in range(len(actual)):
        if actual[digit] == guess[digit]:
            cows.append(1)
        else:
            cows.append(0)
    return cows

def checkBulls(actual, guess, cows):
    bulls = 0
    for digit in range(len(actual)):
        if cows[digit] == 1:
            continue
        elif guess[digit] in actual:
            bulls = bulls + 1
    cow = countCows(cows)
    if cow + bulls > 4:
        bulls = bulls - cow
main()













    for digit in actual
