"""Fortune cookie exercise redux as a structured program."""

from random import randint

<<<<<<< HEAD
__author__ = "720332576"
=======
__author__ = "YOUR 9-DIGIT PID"
>>>>>>> 1e6a345b2b95447229e19d3cf5640ea05677a944


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
<<<<<<< HEAD
    print(fortune_cookie())
=======
>>>>>>> 1e6a345b2b95447229e19d3cf5640ea05677a944
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
<<<<<<< HEAD
def fortune_cookie() -> str:
    """Fortune cookie function, using randint to determine what str to return!"""
    x: int = randint(1, 4)
    if x == 1:
        return("You will find the love of your life this year.")
    else:
        if x == 2:
            return("You will win the lottery this year.")
        else:
            if x == 3:
                return("You will be vaccinated for coronavirus this year.")
            else:
                if x == 4:
                    return("You will pass comp 110 with an A this year.")                
                else:
                    return("")
=======
>>>>>>> 1e6a345b2b95447229e19d3cf5640ea05677a944


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
