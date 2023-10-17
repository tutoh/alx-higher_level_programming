#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []
    
    # Iterate through each row in the input matrix
    for row in matrix:
        squared_row = []
        
        # Iterate through each element in the row and square it
        for num in row:
            squared_row.append(num ** 2)
        
        # Append the squared row to the squared matrix
        squared_matrix.append(squared_row)
    
    return squared_matrix
