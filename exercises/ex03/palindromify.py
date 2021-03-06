"""EX03 - palindromify function."""

__author__: str = "720332576"


def palindromify(x: str, y: bool) -> str:
    """Palindromifies your string."""
    mylist = []
    i = 0
    reverselist = []
    a = len(x)
    if y:
        while i < a:
            mylist.insert(i, x[i])
            reverselist.insert(i, x[i])
            i += 1
        reverselist.reverse()
        palin = mylist + reverselist
        return ''.join(palin)
    else:
        while i < a:
            mylist.insert(i, x[i])
            reverselist.insert(i, x[i])
            i += 1
        reverselist.reverse()
        reverselist.pop(0)
        palin = mylist + reverselist
        return ''.join(palin)
       

def main() -> None:
    """Entrypoint of the program."""
    a = str(input())
    b = bool((len(a) - 1) % 2)
    print(palindromify(a, b))


if __name__ == "__main__":
    main()