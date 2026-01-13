#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        sys.exit(1)

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Please enter a valid integer")
    sys.exit(1)

print(factorial(n))
