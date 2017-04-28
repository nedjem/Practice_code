#!/usr/bin/python3

def rotate_matrix(matrix):
    size = len(matrix)
    new_matrix = [[0 for j in range(size)] for i in range(size)]
    
    for row in range(size):
        for column in range(size):
            new_matrix[column][size-row] =  matrix[row][column]
            
    return new_matrix