"""Tar Heels exercise redux as a structured program."""

<<<<<<< HEAD
__author__ = "720332576"
=======
__author__ = "YOUR 9-DIGIT PID"
>>>>>>> 1e6a345b2b95447229e19d3cf5640ea05677a944


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
<<<<<<< HEAD
    print(tar_heels(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(z: int) -> str: 
    """Takes input and does mod to see what str to return!"""
    a = z % 2
    b = z % 7

    if a == 0 and b == 0:
        return("TAR HEELS")
    else:
        if a == 0:
            return("TAR")
        else:
            if b == 0:
                return("HEELS")
            else:
                return("CAROLINA")
=======


# TODO 1: Define the tar_heels function, and its logic, here.
>>>>>>> 1e6a345b2b95447229e19d3cf5640ea05677a944


if __name__ == "__main__":
    main()
