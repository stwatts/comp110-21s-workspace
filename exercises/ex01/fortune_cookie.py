"""Program that outputs one of at least four random, good fortunes."""

__author__ = "720332576"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
     
# Begin your solution here...
str0: str = "Your fortune cookie says..."
str1: str = "Now, go spread positive vibes!"
x: int = randint(1, 4)
if x == 1:
    print(str0)
    print("You will find the love of your life this year.")
    print(str1)
else:
    if x == 2:
        print(str0)
        print("You will win the lottery this year.")
        print(str1)
    else:
        if x == 3:
            print(str0)
            print("You will be vaccinated for coronavirus this year.")
            print(str1)
        else:
            if x == 4:
                print(str0)
                print("You will pass comp 110 with an A this year.")
                print(str1)
