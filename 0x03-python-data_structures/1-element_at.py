#!/usr/bin/python3

def element_at(my_list, idx):
    # Check if idx is negative
    if idx < 0:
        return None

    # Initialize a variable to keep track of the current index
    current_idx = 0

    # Iterate through the list
    for element in my_list:
        # Check if the current index matches the desired index (idx)
        if current_idx == idx:
            return element
        current_idx += 1

    # If we reach this point, idx is out of range
    return None

# Example usage:
my_list = [1, 2, 3, 4, 5]
idx = 2
result = element_at(my_list, idx)
print(result)  # This will print 3

idx = 10
result = element_at(my_list, idx)
print(result)  # This will print None since idx is out of range
