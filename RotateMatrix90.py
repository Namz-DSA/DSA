def RotateMatrix90(matrix):
    noRows = len(matrix)
    noCols = len(matrix[0])
    transpose_data = []
    rotated_mat = []
    
    for i in range(noCols):
        newRows = []
        for j in range(noRows):
            newRows.append(matrix[j][i])
        transpose_data.append(newRows)
    
    for row in transpose_data:
        row.reverse()
    
    for row in transpose_data:
        rotated_mat.append(row)
    return rotated_mat

print(RotateMatrix90(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
))