"""My first program for COMP110."""
__author__ = "720332576"
print("Hello, world.")



__author__ = "720332576"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(z: int) -> str: 
    """Takes input and does mod to see what str to return!"""
    a = z % 2
    b = z % 7

    if a == 0 and b == 0:
        return(1 + 2 + 3 / 3)
    else:
        if a == 0:
            return(20)
        else:
            if b == 0:
                return(30)
            else:
                return(40)



if __name__ == "__main__":
    main()
