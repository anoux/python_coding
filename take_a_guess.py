# -*- coding: utf-8 -*-
"""
This is a guess the number game
"""

import random

print ("Hello, what's your name?")
name = input()
print ("Well, " + name + ", I am thinking of a number between 1 and 20")
secretnumber = random.randint(1, 20)

for guessestaken in range(1,7):
    print("Take a guess")
    guess = int(input())
    
    if guess < secretnumber:
        print("Your guess is too low")
    elif guess > secretnumber:
        print("your guess is too high")
    else:
        break #this condition is for the correct guess

if guess == secretnumber:
    print("Cheers, " + name + ". You guessed my number in " + str(guessestaken) + " guesses")
else:
    print("That is not the number I was thinking of. It was " + str(secretnumber))    
 