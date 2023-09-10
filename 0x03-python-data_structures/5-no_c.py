#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    length = len(my_string)

    n = 0

    new_string = my_string[:]

    for m in range(length):
        if (my_string[m] == 'c' or my_string[m] == 'C'):
            new_string = new_string[:(m - n)] + my_string[(m + 1):]
            n += 1

    return (new_string)
