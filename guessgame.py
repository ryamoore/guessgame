#!/usr/bin/env python3
#guessgame.py
#Ryan Moore
#10/30/2017
#simple number guessing game

import random

MIN = 1
MAX = 20

targetNumber = random.randint(MIN, MAX)

prompt = "Please guess a number from " + str(MIN) + " to " + str(MAX) + ": "
guess= int(input(prompt))
print(guess)