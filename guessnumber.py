"""
Guess a number game
-------------------
Write a guessing game where the user has to guess a secret number. 
After every guess the program tells the user whether their number 
was too large or too small. At the end the number of tries needed 
should be printed. It counts only as one try if they input the 
same number multiple times consecutively.
"""

from random import seed
from random import randint
from datetime import datetime

def checkInteger(inputNumber):
    num = None
    try:
        num = int(inputNumber)
    except:
        print("Only integer numbers allowed!")
        num = False
    return num

def main():
    top = 100
    guesses = list()
    guessed = False

    seed(datetime.now())
    secret = randint(1,top)
    print ("Guess a number game")
    print ("-------------------")
    print("Let's guess a number between 1 and {}!".format(top))
    print("Enter your guess or \"end\" to finsih")
    while not guessed:
        guess = input("Your guess: ")
        if guess=="end": break
        guess = checkInteger(guess)
        if not guess: continue

        if guess in guesses:
            print("You already tried that!")
        else:
            guesses.append(guess)

        if guess == secret:
            print("You nailed! Congrats")
            guessed = True
        else:
            if guess < secret:
                print("Try a larger number")
            else:
                print("Try a smaller number")
    if guessed:
        print("It took you only {} attempps!".format(len(guesses)))
    else:
        print("Game over!")

if __name__=="__main__":
    main()