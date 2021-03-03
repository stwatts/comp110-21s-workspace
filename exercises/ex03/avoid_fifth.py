"""EX03 - avoid_fifth function."""

__author__: str = "720332576"

def avoid_fifth(x: str) -> str:
    """Removes all e or E characters"""
    y = len(x)
    mylist = []
    i = 0
    while i < y:
        if x[i] != 'e' and x[i] != "E":
            mylist.append(x[i])
            i += 1
        else:
            i += 1
    z: str = ''.join(mylist)
    return z
    

def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth(str(input())))


if __name__ == "__main__":
    main()