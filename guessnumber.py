import random

easyGuess = random.randint(1, 10)
mediumGuess = random.randint(1, 20)
hardGuess = random.randint(1, 50)

print('Welcome to this Random Number Guessing Game, Choose your Level')
chooseLevel = str(input('(E)asy | (M)edium | (H)ard : '))
level = chooseLevel.lower()
count = 0
if level == "e":
    guess_limit = 6
    while count < guess_limit:
        guess = int(input("Guess the Random number between 1 and 10 (6 Guesses Only): "))
        if easyGuess == guess:
            print("You got it right")
            break
        elif easyGuess != guess:
            print("That was Wrong! Guesses Left :" + str((guess_limit - count) - 1))
        count += 1
        if count == guess_limit:
            print("Game Over! The Correct Number is " + str(easyGuess))

if level == "m":
    guess_limit = 4
    while count < guess_limit:
        guess = int(input("Guess the Random number between 1 and 20 (4 Guesses Only): "))
        if mediumGuess == guess:
            print("You got it right")
            break
        elif mediumGuess != guess:
            print("That was Wrong! Guesses Left :" + str((guess_limit - count) - 1))
        count += 1
        if count == guess_limit:
            print("Game Over! The Correct Number is " + str(mediumGuess))

if level == "h":
    guess_limit = 3
    while count < guess_limit:
        guess = int(input("Guess the Random number between 1 and 50 (3 Guesses Only): "))
        if hardGuess == guess:
            print("You got it right")
            break
        elif hardGuess != guess:
            print("That was Wrong! Guesses Left :" + str((guess_limit - count) - 1))
        count += 1
        if count == guess_limit:
            print("Game Over! The Correct Number is " + str(hardGuess))


