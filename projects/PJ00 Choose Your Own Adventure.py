"""PJ00-Choose Your Own Adventure"""

__author__ = "720332576"

from random import randint

player: str
points: int
MAKEITRAIN: str = "\U0001F4B8"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    greet()
    choosegame()

def greet() -> None:
    """Greets the players."""
    print("Hello, what is your name?")
    global player
    global points
    global MAKEITRAIN
    player = input()
    print(f"Welcome {player}, we are glad you are here.")
    print(f"You have been awarded 100 points to spend. Use them wisely {MAKEITRAIN}")
    points = 100

def choosegame() -> None:
    """The player chooses which minigame to play."""
    print("Which minigame would you like to play? \n a-High Card/Low Card \n b-Guess The Number \n c-Quit")
    global points
    global MAKEITRAIN
    x: str = input()
    if x == "a" or x == "A":
        hilowgreet()
    else:
        if x == "b" or x == "B":
            guessnumbergreet()
        else:
            if x == "c" or x == "C":
                print(f"Thank you for playing, {player}!")
                print(f"You ended with {points} points {MAKEITRAIN}")
                return()
            else:
                print("You have entered an incorrect command. Please try again")
                choosegame()
            

    
def hilowgreet() -> None:
    """High Card Low Card Minigame."""
    print("Welcome to High Card/Low Card")
    print("Dual against the computer. Highest card wins!")
    print("Unlike the casino, the odds are slightly in your favor!")
    hilow()

def hilow() -> None:
    """Hi/low card game."""
    print("How many points would you like to wager?")
    global points
    global MAKEITRAIN
    print(f"You currently have {points} points {MAKEITRAIN}")
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Please input a number")
        else:
            y: int
            z: int
            if x <= points:
                print(f"You wagered {x} points")
                y = randint(1,10)
                z = randint(1,10)
                print(f"You drew a {y}")
                print(f"The computer drew a {z}")
                if y >= z:
                    points =  points + x
                    print(f"You win! You have earned {x} points. You now have {points} points {MAKEITRAIN}")
                    choosegame()
                else:
                    points = points - x
                    print(f"You lose! You lost {x} points. You now have {points} points {MAKEITRAIN}")
                    if points <= 0:
                        print("You ran out of points! Game over!")
                        outofpoints()
                    else: choosegame()
            else:
                print("You don't have enough points")
            break


def guessnumbergreet() -> None:
    """Guess the number game greeting."""
    print("Welcome to Guess The Number")
    print("Guess the correct number in the fewest number of guesses")
    print("If you correctly guess in 10 or less tries then you win! Otherwise, you lose your wager.")
    print("Values range from 1-100. Good luck!")
    guessnumber()

def guessnumber() -> None:
    """Guess the number minigame."""
    print("How many points would you like to wager?")
    global points
    global MAKEITRAIN
    print(f"You currently have {points} points {MAKEITRAIN}")
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Please input a number")
        else:
            y: int = randint(1,5)
            z: int = 0
            count: int = 0
            if x <= points:
                print(f"Your wager is {x} points {MAKEITRAIN}")
            else:
                print("You don't have enough points")
                guessnumber()
            while y != z:
                print("What is your guess?")
                z=int(input())
                count = count + 1
                if y == z:
                    print("You guessed it!")
                    print(f"It took you {count} guesses")
                    if count == 1:
                        a = 10 * x
                        points = points + a
                        print(f"You hit the jackpot! You win {a} points! {MAKEITRAIN}")
                        print(f"You now have {points} points. {MAKEITRAIN}")
                    elif count <= 8:
                        a = 2 * x
                        points = points + a
                        print(f"You win {a} points!")
                        print(f"You now have {points} points.")
                    elif count <= 10:
                        a = x
                        points = points + a
                        print(f"You win {a} points!")
                        print(f"You now have {points} points.")
                    elif count > 10:
                        a = x
                        points = points - a
                        print(f"You lost {a} points!")
                        print(f"You now have {points} points.")
                    break
                elif y > z:
                    print("Try a higher number")
                elif z > y:
                    print("Try a lower number")
            break
    choosegame()
   

def outofpoints() -> None:
    """If point balance equals 0 or less then end game."""
    global points
    global player
    print("Would you like to continue? Y/N")
    x = input()
    if x == "Y" or x == "y":
        print("Here are an additional 50 points to spend.")
        points = points + 50
        print("Please try not to lose them all this time.")
        choosegame()
    elif x == "N" or x == "n":
        print(f"Thanks for playing, {player}!")
    else:
        print("You have entered an incorrect command. Please try again.")
        outofpoints()

if __name__ == "__main__":
    main()
