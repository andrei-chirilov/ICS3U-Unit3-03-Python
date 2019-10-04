#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program plays the guessing game


import constant


def main():

    # asking if they can guess my number that I choose between 0 and 10

    print("Can you guess the number I chose from 0 to 10?")

    # Input
    number = int(input("Enter the number that you think I guessed: "))

    # process
    if number == (constant.constant):
        print("You guessed it :)")
    else:
        print("The correct number was 5")


if __name__ == "__main__":
    main()
