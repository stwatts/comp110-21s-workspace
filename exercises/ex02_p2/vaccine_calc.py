"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "720332576"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    x: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    y: str = future_date(x)
    # TODO 5: Print the expected output using the variables above.
    print(str(x))
    print(y.strftime("%B %d, %Y"))


# TODO 1: Define days_to_target function
def days_to_target(a: int, b: int, c: int, d: int) -> int:
    """How many days to target?"""
    x: float = a * (d / 100)
    y: float = x - 0.5 * b
    z: int = round((2 * y / c))
    return(z)


# TODO 3: Define future_date function
def future_date(a: int) -> str:
    """Gives expected date to reach targeted population."""
    today: datetime = datetime.today()
    remaining: timedelta = timedelta(a)
    difference: datetime = today + remaining
    return(str(difference))


if __name__ == "__main__":
    main()
