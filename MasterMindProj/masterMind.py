from random import randint

def generateNum():
    actual = randint(0000, 9999)
    return actual

def getGuess():
    guess = -1
    while guess < 0 or guess >= 10000:
        guess = raw_input("Guess a number betweeen 0000 and 9999:")
        guess = int(guess)
    return guess

def main():
    actual = generateNum()
    print str(actual)
    actual_Array = convertToArray(actual)
    guess = getGuess()
    guess_Array = convertToArray(guess)
    turns = 1
    while actual != guess:
        actual_Array = convertToArray(actual)
        cows_Arr = checkCows(actual_Array, guess_Array)
        bulls = checkBulls(actual_Array, guess_Array, cows_Arr)
        cows = countCows(cows_Arr)
        print "Your guess generated " + str(cows) + " cows and " + str(bulls) + " bulls."
        guess = getGuess()
        guess_Array = convertToArray(guess)
        turns = turns + 1;
    print "You guessed it! And it only too you " + str(turns) + " guess!"

def convertToArray(num):
    if len(str(num)) < 2:
        arr = [0,0,0, num]
        return arr
    elif len(str(num)) < 3:
        arr = [0,0]
    elif len(str(num)) < 4:
        arr = [0]
    convert = str(num)
    arr = []
    for digit in list(convert):
        arr.append(digit)
    return arr

def countCows(arr):
    i = 0
    for num in range(4):
        if arr[num] == 1:
            i = i + 1
    return i

def checkCows(actual, guess):
    cows = []
    for digit in range(len(actual)):
        if actual[digit] == guess[digit]:
            cows.append(1)
            actual[digit] = 'f'
        else:
            cows.append(0)
    return cows

def checkBulls(actual, guess, cows):
    bulls = 0
    for digit in range(4):
        if cows[digit] == 1:
            continue
        else:
            if guess[digit] in actual:
                    bulls = bulls + 1
                    actual[actual.index(guess[digit])] = 'f'
    cow = countCows(cows)
    if cow + bulls > 4:
        bulls = bulls - cow
    return bulls
main()
