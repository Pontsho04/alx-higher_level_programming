#!/usr/bin/python3
# 8-uppercase.py

def uppercase(input_str):
    """Print a string in uppercase."""
    modified_str = ""
    for c in input_str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            modified_str += c

            print(modified_str)
