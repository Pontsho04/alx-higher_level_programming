#!/usr/bin/python3

def multiply_list_map(my_list=None, number=1):
    if my_list is None:
        my_list = []
    return list(map(lambda i: i * number, my_list))
