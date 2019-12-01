#!/usr/bin/env python3

"""
https://adventofcode.com/2019/day/x
"""

def main():

    with open("input.txt", 'r') as input_file:
        ints = [int(x) for x in input_file.readlines()]

    isum = 0

    for i in ints:
        isum += i

    print(isum)

if __name__ == "__main__":
    main()
