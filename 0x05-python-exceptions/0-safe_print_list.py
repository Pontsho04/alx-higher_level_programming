#!/usr/bin/python3

def print_elements(my_list=[], x=0):
    """Print x elements from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements from my_list to print.

    Returns:
        int: The number of elements actually printed.
    """
    elements_printed = 0
    for item in my_list[:x]:
        print(item)
        elements_printed += 1
    return elements_printed
