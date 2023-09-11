#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Get the element at the specified index in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the element to retrieve.

    Returns:
        object: The element at the specified index, or None if the index is out of range.
    """
    if idx < 0:
        return None

    length = len(my_list)

    if idx > length - 1:
        return None

    return my_list[idx]
