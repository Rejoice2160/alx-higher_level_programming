#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if n != 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][n]), end='')
        print()
