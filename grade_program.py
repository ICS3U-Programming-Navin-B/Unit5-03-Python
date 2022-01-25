#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 20 2022
# This program uses a function to calculate
# the user"s grade percentage.


def find_percent(grade):
    # switch/case workaround
    grades = {
        # Don't know what lambda does, but the
        # code doesn't work without it.
        "4+": lambda: 98,
        "4": lambda: 90,
        "4-": lambda: 83,
        "3+": lambda: 78,
        "3": lambda: 75,
        "3-": lambda: 71,
        "2+": lambda: 68,
        "2": lambda: 65,
        "2-": lambda: 61,
        "1+": lambda: 58,
        "1": lambda: 55,
        "1-": lambda: 51,
        "R": lambda: 25,
    }
    # return variable value
    return grades.get(grade, lambda: -1)()


def main():
    # get input
    grade_input = input("Enter your grade : ")

    # call function
    percentage = find_percent(grade_input)

    # error checking
    if percentage == -1:
        print("Invalid input.")
    else:
        print("Your percentage is {}%.". format(percentage))


if __name__ == "__main__":
    main()
