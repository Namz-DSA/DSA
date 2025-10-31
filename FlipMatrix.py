def FlipMatrix(matrix):
    noRows = len(matrix)
    vert_mat = []

    for i in range(noRows-1,-1,-1):
        vert_mat.append(matrix[i])
    return vert_mat

print(FlipMatrix(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
))