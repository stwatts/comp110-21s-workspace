"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

import math

today: datetime = datetime.today()

print("Please enter the population")
Population = int(input())
print("Please enter the total number of vaccine doses that have already been administered")
Administered = int(input())
print("Please enter the number of doses given per day")
Rate = int(input())
print("Please enter desired percent of population to be vaccinated")
Target = int(input())


Target_population: int = Population * (Target/100)
Population_remaining: int = Target_population - 0.5 * Administered
Days_remaining: int = math.ceil(2 * Population_remaining / Rate) 

remaining: timedelta = timedelta(Days_remaining)

future: datetime = today + remaining

print("Population: " + str(Population))
print("Doses administered: " + str(Administered))
print("Doses per day: " + str(Rate))
print("Target percent vaccinated " + str(Target))

print("We will reach " + str(Target) + "% vaccination in " + str(Days_remaining) + " days, which falls on " + future.strftime("%B %d, %Y") + ".")



