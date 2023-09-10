#!/usr/bin/python3
10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    check_div = []

    for m in range(len(my_list)):
        if my_list[m] % 2 == 0:
            check_div.append(True)
        else:
            check_div.append(False)

    return (check_div)
