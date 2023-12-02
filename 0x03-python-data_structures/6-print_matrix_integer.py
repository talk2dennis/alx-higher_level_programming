#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for numlist in matrix:
        for j in range(len(numlist)):
            print("{:d}".format(numlist[j]), end="")
            if j < len(numlist) - 1:
                print("", end=" ")
        print()
