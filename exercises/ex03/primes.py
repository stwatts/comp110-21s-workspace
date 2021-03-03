"""EX03 - prime functions."""

__author__: str = "720332576"


def is_prime(x: int) -> bool:
    """Determines if input is a prime number or not."""
    if x < 2:
        return False
    i = 2
    mylist = []
    while i < x:
        a = x % i
        mylist.append(a)
        i += 1
    count = mylist.count(0)
    if count == 0:
        return True
    else:
        return False
        

def list_primes(x: int, y: int) -> list[int]:
    """Returns all prime numbers between two parameters."""
    myrange = []
    i = 0
    if x < 2:
        x = 2
    while i < y - x:
        myrange.append(x + i)
        i += 1
    j = 0
    myprimes = []
    while j < len(myrange):
        a = is_prime(myrange[0 + j])
        myprimes.append(a)
        j += 1
    h = 0
    allprimes = []
    while h < len(myprimes):
        if myprimes[h]:
            allprimes.append(myrange[h])
        h += 1
    return allprimes


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(int(input())))
    a = int(input())
    b = int(input())
    print(list_primes(a, b))
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))


if __name__ == "__main__":
    main()