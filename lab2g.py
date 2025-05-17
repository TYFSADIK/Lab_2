#!/usr/bin/env python3
# lab2g.py - Countdown with default argument if none provided

import sys

if len(sys.argv) == 2:
    counter = int(sys.argv[1])
else:
    counter = 3  # default value when no arguments are provided

while counter > 0:
    print(counter)
    counter -= 1

print("blast off!")

