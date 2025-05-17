#!/usr/bin/env python3
# lab2f.py - Countdown from provided number using command-line arguments

import sys

if len(sys.argv) != 2:
    print("Usage: ./lab2f.py number")
    sys.exit(1)

counter = int(sys.argv[1])

while counter > 0:
    print(counter)
    counter -= 1

print("blast off!")

