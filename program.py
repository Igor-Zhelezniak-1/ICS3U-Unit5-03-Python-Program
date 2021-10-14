#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def mark(number):
    # calculate mark
    if number == "R":
        mark = 25
    elif number == "1-":
        mark = 51
    elif number == "1":
        mark = 54
    elif number == "1+":
        mark = 58
    elif number == "2-":
        mark = 61
    elif number == "2":
        mark = 65
    elif number == "2+":
        mark = 68
    elif number == "3-":
        mark = 71
    elif number == "3":
        mark = 75
    elif number == "3+":
        mark = 78
    elif number == "4-":
        mark = 83
    elif number == "4":
        mark = 90
    elif number == "4+":
        mark = 98
    else:
        mark = "r"

    return mark


def main():
    # input
    number_from_user = input("Enter the level you want converted to a percentage: ")

    # called function
    calculated_mark = mark(number_from_user)

    # output
    try:
        calculated_mark1 = int(calculated_mark)
        print(
            "Level {0} has a middle percentage of {1}%".format(
                number_from_user, calculated_mark1
            )
        )

    except Exception:
        print("-1. Invalid input")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
