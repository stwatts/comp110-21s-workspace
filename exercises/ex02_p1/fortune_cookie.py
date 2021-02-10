"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "720332576"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
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
                


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
