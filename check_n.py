#!/bin/python

# import sys


# N = int(raw_input().strip())


def check_n(n):
    while n in range(1, 101):
        if n % 2 != 0:
            return "Weird"
        elif n % 2 == 0 and n in range(2, 6):
            return "Not Weird"
        elif n % 2 == 0 and n in range(6, 21):
            return "Weird"
        else:
            return "Not Weird"


print check_n(4)
