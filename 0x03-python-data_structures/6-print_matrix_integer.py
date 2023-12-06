#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for SubMatrix in matrix
        if len(SubMatrix) == 0:
            print()
    for i range(len(SubMatrix)):
        print("{:d}".format(SubMatrix[i])),
            end="\n" if i is len(SubMatrix) - 1 else " ")
