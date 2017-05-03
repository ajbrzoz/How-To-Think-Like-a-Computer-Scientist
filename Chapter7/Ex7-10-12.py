# Exercise 7.10.12

# A year is a leap year if it is divisible by 4 unless it is a century that is not divisible by 400.
# Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.


def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
      return True
    else:
      return False

