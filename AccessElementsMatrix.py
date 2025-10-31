def AccessElements(matrix):
    #Access element at 2nd row, 3rd column
    print(matrix[1][2])
    print(matrix[0])
    print([row[2] for row in matrix])

AccessElements([[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])