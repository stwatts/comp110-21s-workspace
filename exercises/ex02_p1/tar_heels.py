"""Tar Heels exercise redux as a structured program."""

__author__ = "720332576"

def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(z:int) -> str:
#takes input and does mod to see what str to return
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

if __name__ == "__main__":
    main()

    