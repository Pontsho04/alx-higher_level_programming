#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}{}".format(uppercase_char, char), end='')
        else:
            print(char, end='')
    print()
